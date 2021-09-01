from django.contrib import admin
from . models import *
from django.contrib.auth.models import Group
admin.site.site_header = 'Sampurna Mart'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','category','quantity')
    list_filter =('category',)
admin.site.register(Product,ProductAdmin)
# admin.site.unregister(Group)

admin.site.register(Order)

