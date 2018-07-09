from django.contrib import admin
from django.urls import include, path, url
from django.views.generic import RedirectView, TemplateView

from django_markdown import urls as markdown_urls
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from floreal import views as floreal_views


urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^accounts/register$', floreal_views.user_register, name="user_register"),
    url(r'^accounts/registration_post.html$', floreal_views.user_register_post, name="registration_post"),
    url(r'^accounts/password/reset/?$', floreal_views.password_reset, name="password_reset"),
    url(r'^add-phone-number/(?P<phone>[^./]+)$', floreal_views.phone.add_phone_number, name="add_phone_number"),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('pages/', include(wagtail_urls)),
    path('markdown/', include(markdown_urls)),

    path('videgrenier/', include('videgrenier.urls')),
    path('vide-grenier/', RedirectView.as_view(url='/videgrenier/', permanent=True)),

    path('circuitscourts/' (include('floreal.urls')),

    path('', TemplateView.as_view(template_name='base.html')),
]
