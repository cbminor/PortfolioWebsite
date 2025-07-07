from django.db import models

from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import PageChooserPanel


LINK_TYPES = [
    ('GitHub', 'GitHub'),
    ('Kaggle', 'Kaggle'),
    ('Tableau', 'Tableau')
]

CARD_COLORS = [
    ("Orange", "#ac5625"),
    ("Beige", "#b48351"),
    ("Tan", "#b5aba6"),
    ("Brown", "#483a2b"),
    ("Gray", "#666666")
]

@register_snippet
class ProjectCard(models.Model):
    project_title = models.CharField(
          blank=True,
          max_length=255,
          help_text="The display title for the project"
    )

    project_summary = models.CharField(
          blank=True,
          max_length=255,
          help_text="A short summary of the project (About 100 characters)"
    )

    project_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Project Image"
    )    
    
    project_link = models.URLField(max_length = 200, blank=True)

    project_link_type = models.CharField(max_length=10, choices=LINK_TYPES, blank=True)

    blog_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Choose the related blog page"
        )

    panels = [
        FieldPanel("project_title"),
        FieldPanel("project_summary"),
        FieldPanel("project_image"),
        FieldPanel("project_link"),
        FieldPanel("project_link_type"),
        PageChooserPanel("blog_link")
    ]

    def __str__(self):
        return self.project_title
