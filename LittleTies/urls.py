from django.contrib import admin
from django.urls import path,include


admin.site.site_header = "LittleTies-Admin"
admin.site.site_title = "LittleTies-Admin Portal"
admin.site.index_title = "Welcome to LittleTies-Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('website.urls')),
    path("accounts/",include("allauth.urls"))
]