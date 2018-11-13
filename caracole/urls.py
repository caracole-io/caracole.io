from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView, TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('agenda', TemplateView.as_view(template_name='agenda.html'), name='agenda'),  # TODO
    path('blog', TemplateView.as_view(template_name='blog.html'), name='blog'),  # TODO
    path('liens', TemplateView.as_view(template_name='liens.html'), name='liens'),  # TODO
    path('videgrenier/', include('videgrenier.urls')),
    path('vide-grenier/', RedirectView.as_view(url='/videgrenier/', permanent=True)),
    path('', include(wagtail_urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
