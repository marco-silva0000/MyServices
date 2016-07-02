from django.contrib import admin

from .models import *


# Register your models here.


class AdminClasses(admin.ModelAdmin):
    pass


admin.site.register(Car, AdminClasses)
admin.site.register(FuelCharge, AdminClasses)
