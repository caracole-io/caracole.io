from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView

from . import models


class CaramelView(CreateView):
    model = models.Caramel
    fields = ["mail"]

    def form_valid(self, form):
        messages.success(
            self.request, "Votre inscription au Caramel a bien été prise en compte"
        )
        return super().form_valid(form)


def mail_contact(request):
    if request.method == "POST":
        print(request.POST)

        print(
            f'To: {request.POST["form_dest"]}@{settings.PROJECT}.{settings.DOMAIN_NAME}'
        )
        print(f'Reply-To: {request.POST["form_name"]} <{request.POST["form_adress"]}>')
        print("Subject: Message envoyé depuis le site")
        print()
        print(request.POST["form_message"])
        messages.success(request, "Votre message a bien été envoyé")
    return redirect("/contacts/")
