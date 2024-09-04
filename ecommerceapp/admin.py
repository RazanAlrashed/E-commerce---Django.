from django.contrib import admin
from .models import items,storetype,itemdetails,cart
# Register your models here.
admin.site.register(storetype)
admin.site.register(items)
admin.site.register(itemdetails)
admin.site.register(cart)