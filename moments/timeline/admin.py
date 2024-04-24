from django.contrib import admin
from .models import Photo


# class MomentsAdminSite(admin.AdminSite):
#     site_header = "Moments administration"
#     site_title = "Moments admin"


# admin_site = MomentsAdminSite(name="myadmin")
# admin_site.register(Photo)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "image", "place", "time")

admin.site.register(Photo, PhotoAdmin)
