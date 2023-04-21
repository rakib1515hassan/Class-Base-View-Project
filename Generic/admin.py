from django.contrib import admin
from .models import Player
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    fields = ("pic","name", "age", "play", "position", "admin_photo")
    list_display = ["admin_photo","name", "age", "play", "position", "slug"]
    #date_hierarchy = 'publish_date'
    readonly_fields = ['admin_photo']

    
# admin.site.register(Player, PlayerAdmin)