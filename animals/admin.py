from django.contrib import admin

from .models import Animal, Review

class AnimalAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Animal, AnimalAdmin)

admin.site.register(Review)