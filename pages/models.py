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
    href = models.URLField('lien', blank=True, null=True)

    panels = [FieldPanel('title'), FieldPanel('text'), FieldPanel('href'), ImageChooserPanel('img')]


class CaraPage(Page):
    nom = models.CharField(max_length=250)
    img = models.ForeignKey('wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    img_caption = models.CharField('légende de l’image', max_length=250, blank=True, null=True)
    exergue = models.TextField(blank=True, null=True)
    citation = models.CharField('auteur de l’exergue', max_length=250, blank=True, null=True)
    content = RichTextField('contenu', blank=True)

    search_fields = Page.search_fields + [
        index.SearchField(field) for field in ['nom', 'img_caption', 'exergue', 'citation', 'content']
    ]
    content_panels = Page.content_panels + [ImageChooserPanel('img')] + [
        FieldPanel(field) for field in ['nom', 'img_caption', 'exergue', 'citation', 'content']
    ] + [InlinePanel('rubriques', label='Rubriques')]


class Rubrique(Orderable):
    page = ParentalKey(CaraPage, on_delete=models.CASCADE, related_name='rubriques')
    title = models.CharField('titre', max_length=250)
    content = RichTextField('contenu', blank=True)


class Section(Page):
    pass


class Contact(Page):
    content = RichTextField('contenu', blank=True)

    content_panels = Page.content_panels + [FieldPanel('content', classname='full')]


class Liens(CaraPage):
    content_panels = CaraPage.content_panels + [InlinePanel('amis', label='Amis')]


class Amis(Orderable):
    page = ParentalKey(CaraPage, on_delete=models.CASCADE, related_name='amis')
    logo = models.ForeignKey('wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+')
    title = models.CharField('titre', max_length=250)
    href = models.URLField('lien', blank=True, null=True)

    panels = [FieldPanel('title'), FieldPanel('href'), ImageChooserPanel('logo')]
