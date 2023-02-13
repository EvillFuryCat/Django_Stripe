from django.contrib import admin
from .models.item import Item


class PaymentSystemSite(admin.AdminSite):
    pass


payment_system_site = PaymentSystemSite(name="Payment System admin")


@admin.register(Item, site=payment_system_site)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
