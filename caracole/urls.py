from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),

    path('videgrenier/', include('videgrenier.urls')),
    path('vide-grenier/', RedirectView.as_view(url='/videgrenier/', permanent=True)),

    path('', TemplateView.as_view(template_name='base.html')),
]
