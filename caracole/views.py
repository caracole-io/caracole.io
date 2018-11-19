from django.views.generic import CreateView, DetailView, RedirectView, TemplateView

from . import models


class CaramelView(CreateView):
    model = models.Caramel
    fields = ['mail']
