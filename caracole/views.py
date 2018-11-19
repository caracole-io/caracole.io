from django.contrib import messages
from django.views.generic import CreateView, DetailView, RedirectView, TemplateView

from . import models


class CaramelView(CreateView):
    model = models.Caramel
    fields = ['mail']

    def form_valid(self, form):
        messages.success(self.request, 'Votre inscription au Caramel a bien été prise en compte')
        return super().form_valid(form)
