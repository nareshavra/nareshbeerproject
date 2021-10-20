from django.contrib import admin
from testapp.models import BeerModel

# Register your models here.
class BeerAdmin(admin.ModelAdmin):
    list_display=['name','coo','price','taste','poa']

admin.site.register(BeerModel,BeerAdmin)
