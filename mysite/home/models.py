from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from blog.models import BlogPage, BlogIndexPage


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    @property
    def get_newest_articles(self):
        articles = BlogPage.objects.live()
        articles = articles.order_by('-date')[:3]
        return articles

    @property
    def get_all_articles_page(self):
        return BlogIndexPage.objects.all()[0]

