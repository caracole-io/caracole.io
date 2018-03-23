from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('videgrenier/', include('videgrenier.urls')),

    path('', TemplateView.as_view(template_name='base.html')),
]
