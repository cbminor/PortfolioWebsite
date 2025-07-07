from django.db import models
from wagtail import blocks
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import (
    FieldPanel,
    FieldRowPanel,
    InlinePanel,
    MultiFieldPanel,
)
from modelcluster.fields import ParentalKey
from wagtail.images.blocks import ImageBlock
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.api import APIField
from home.blocks import ThreeCardDisplayBlock, CustomImageBlock

STYLE_TYPES = [
    ("Inline", "Inline"),
    ("Block", "Block")
]

@register_setting
class NavigationSettings(BaseGenericSetting):
    linkedin_url = models.URLField(verbose_name="LinkedIn URL", blank=True)
    github_url = models.URLField(verbose_name="GitHub URL", blank=True)
    kaggle_url = models.URLField(verbose_name="Kaggle URL", blank=True)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("linkedin_url"),
                FieldPanel("github_url"),
                FieldPanel("kaggle_url"),
            ],
            "Social settings",
        )
    ]


class HomePage(Page):
    """ The Home Page """

    home_title = models.CharField(
          blank=True,
          max_length=255,
          help_text="Add a title to the front page"
    )

    home_subtitle = models.CharField(
          blank=True,
          max_length=255,
          help_text="Add a subtitle to the front page"
    )

    content = StreamField([
        ("ThreeCardPanel", ThreeCardDisplayBlock())
    ], blank=True)


    subpage_types = [
        'home.AboutPage', 'home.Portfolio', 'blog.ArticleList', 'home.ContactPage'
    ]

    parent_page_type = []

    
    content_panels = Page.content_panels + [FieldPanel("home_title"), 
                                            FieldPanel("home_subtitle"),
                                            FieldPanel("content")]


class ProjectList(Orderable, models.Model):
    page = ParentalKey('home.Portfolio', on_delete=models.CASCADE, related_name='project_list')
    project = models.ForeignKey('home.ProjectCard', on_delete=models.CASCADE, related_name='+')

    class Meta(Orderable.Meta):
        verbose_name = 'project_list'
        verbose_name_plural = 'project_lists'
    
    panels = [
        FieldPanel('project')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.project.project_title
    

class Portfolio(Page):

    intro = models.CharField(
          blank=True,
          max_length=255,
          help_text="A short paragraph introducing the portfolio"
    )

    content_panels = Page.content_panels + [
        'intro',
        InlinePanel('project_list', label="Projects")
    ]

    subpage_types = []
    
    parent_page_type = [
        'home.HomePage' 
    ]

class AboutPage(Page):

    about_text = StreamField([
        ('text', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed', 'code', 'blockquote'])),
        ('image', CustomImageBlock()),
        ('image_left', blocks.StructBlock([
             ('image_left', ImageBlock()),
             ('text_right', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed', 'code', 'blockquote']))
         ])),
        ('image_right', blocks.StructBlock([
             ('text_left', blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'embed', 'code', 'blockquote'])),
             ('image_right', ImageBlock())
         ]))
    ])

    content_panels = Page.content_panels + [FieldPanel("about_text")]

    subpage_types = []
    
    parent_page_type = [
        'home.HomePage' 
    ]

class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', on_delete=models.CASCADE, related_name='form_fields')

    display = models.CharField(max_length=10, choices=STYLE_TYPES, default="Block")

    panels = AbstractFormField.panels + ['display']

    api_fields = AbstractFormField.api_fields + [APIField("display")]


class ContactPage(AbstractEmailForm):
    intro = RichTextField(blank=True)
    contact_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Image for contact page"
    )
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        'contact_image',
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address'),
                FieldPanel('to_address'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_form_fields(self):
        return self.form_fields.all()
