"""
URL configuration for moments project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views
# from timeline.admin import admin_site

urlpatterns = [
    path("timeline/", include("timeline.urls")),
    path('admin/', admin.site.urls),
    path("", views.index, name="home"),
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path("media/photos/<str:img_path>", views.protected_media, name="protected_media"),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
