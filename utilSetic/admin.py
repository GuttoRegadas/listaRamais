from django.contrib import admin

from .models import Ramais

@admin.register(Ramais)
class RamisAdmin(admin.ModelAdmin):
    list_display = ()
    fields = []