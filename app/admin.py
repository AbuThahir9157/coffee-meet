from django.contrib import admin
from . models import Cofeee

# Register your models here.

class CofeeeAdmin(admin.ModelAdmin):
    list_display=('name','price','quantity','image')

admin.site.register(Cofeee,CofeeeAdmin)