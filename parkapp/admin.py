from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Location)
admin.site.register(ParkSlot)
admin.site.register(BookedSlot)
