from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageBlock

class ArticleList(Page):

    heading = models.CharField(
        blank=True,
        max_length=100,
        help_text="The displayed title for the portfolio")
    
    intro = models.CharField(
        blank=True,
        max_length=255,
        help_text="A short introduction to the blog."
    )

    subpage_types = ['blog.BlogEntry']
    
    parent_page_type = [
        'home.HomePage' 
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        # Add extra variables and return the updated context
        context['articles'] = BlogEntry.objects.child_of(self).live()
        return context
    
    content_panels = Page.content_panels + ["heading", "intro"]


class BlogEntry(Page):

    article_title = models.CharField(
          blank=True,
          max_length=255,
          help_text="The title of the article (will appear on the list page)"
    )

    article_summary = models.CharField(
          blank=True,
          max_length=255,
          help_text="A short summary of the article (will be shown on the blog card)"
    )

    article_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Main article image (to be shown on the blog card)"
    )    
    
    article_text = StreamField([
        ('text', blocks.RichTextBlock()),
        ('image', ImageBlock()),
        ('image_left', blocks.StructBlock([
             ('image_left', ImageBlock()),
             ('text_right', blocks.RichTextBlock())
         ])),
        ('image_right', blocks.StructBlock([
             ('text_left', blocks.RichTextBlock()),
             ('image_right', ImageBlock())
         ]))
    ])

    content_panels = Page.content_panels + ["article_title", "article_summary", "article_image", FieldPanel("article_text")]

    subpage_types = []
    
    parent_page_type = [
        'blog.ArticleList' 
    ]