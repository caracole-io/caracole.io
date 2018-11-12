from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class Accueil(Page):
    body = RichTextField('texte', blank=True)

    search_fields = Page.search_fields + [index.SearchField('body')]
    content_panels = Page.content_panels + [
        FieldPanel('body', classname='full'),
        InlinePanel('carousels', label='Carousel')
    ]


class Carousel(Orderable):
    page = ParentalKey(Accueil, on_delete=models.CASCADE, related_name='carousels')
    img = models.ForeignKey('wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+')
    title = models.CharField('titre', max_length=250)
    text = models.CharField('texte', max_length=250)
    href = models.URLField('lien', null=True, blank=True)

    panels = [FieldPanel('title'), FieldPanel('text'), FieldPanel('href'), ImageChooserPanel('img')]
