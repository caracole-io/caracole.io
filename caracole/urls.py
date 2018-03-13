from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from wagtail.core import urls as wagtail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include(wagtail_urls)),

    path('', TemplateView.as_view(template_name='base.html')),
]
