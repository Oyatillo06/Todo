from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    search_fields = ["id","title"]
    list_display = ["title","joy"]
    ordering = ["vaqt"]