from django.contrib import admin
from website.models import *


# My Backend


admin.site.register(user_table)
admin.site.register(agency_table)
admin.site.register(CustomUser)