from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Post)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Post._meta.get_fields() if field.name != "slug"]
