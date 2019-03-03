from django.contrib import admin
from cars.models import Car
from cars.models import Engine
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display=["brand", "model", "year"]
    search_fields=['brand']
    list_filter = ["brand","model"]
#admin.site.register(Car, CarAdmin)

@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ["type", "power"]