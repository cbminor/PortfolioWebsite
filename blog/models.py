from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageBlock
from home.blocks import CustomImageBlock, TwoColumnTextBlock

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

        all_articles = BlogEntry.objects.child_of(self).live().order_by("-first_published_at")
        paginator = Paginator(all_articles, 5)
        page = request.GET.get("page")
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)
        context['articles'] = articles
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
        ('image', CustomImageBlock()),
        ('image_left', blocks.StructBlock([
             ('image_left', ImageBlock()),
             ('text_right', blocks.RichTextBlock())
         ])),
        ('image_right', blocks.StructBlock([
             ('text_left', blocks.RichTextBlock()),
             ('image_right', ImageBlock())
         ])),
         ('two_columns', TwoColumnTextBlock())
    ])

    content_panels = Page.content_panels + ["article_title", "article_summary", "article_image", FieldPanel("article_text")]

    subpage_types = []
    
    parent_page_type = [
        'blog.ArticleList' 
    ]

    def get_context(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        # Add extra variables and return the updated context
        context["next_article"] = BlogEntry.objects.live().filter(first_published_at__lt=self.first_published_at).order_by("first_published_at").last()
        context["previous_article"] = BlogEntry.objects.live().filter(first_published_at__gt=self.first_published_at).order_by("first_published_at").first()
        return context