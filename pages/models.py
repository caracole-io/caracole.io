from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.search import index


class DefaultPage(Page):
    body = RichTextField()

    search_fields = Page.search_fields + [index.SearchField('body')]
    content_panels = Page.content_panels + [FieldPanel('body')]
