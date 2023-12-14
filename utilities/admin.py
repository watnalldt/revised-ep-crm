from django.contrib import admin

from utilities.models import Supplier, Utility


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Utility)
class UtilityAdmin(admin.ModelAdmin):
    pass
