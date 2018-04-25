from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('videgrenier/', include('videgrenier.urls')),
    path('vide-grenier/', RedirectView.as_view(url='/videgrenier/', permanent=True)),

    path('', TemplateView.as_view(template_name='base.html')),
]
