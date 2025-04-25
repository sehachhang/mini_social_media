from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("home/", include("mini_socialmedia.urls")),
    path("", RedirectView.as_view(url=reverse_lazy('home'), permanent=True)),  # default root
]