from django.contrib import admin
from .models import Legend, Trophy, HistoryMilestone


@admin.register(Legend)
class LegendAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'years_at_club', 'order']
    list_editable = ['order']
    list_filter = ['position']
    search_fields = ['name', 'description']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'position', 'years_at_club', 'image', 'order')
        }),
        ('Детали', {
            'fields': ('description', 'achievements')
        }),
    )


@admin.register(Trophy)
class TrophyAdmin(admin.ModelAdmin):
    list_display = ['name', 'competition', 'count']
    list_filter = ['competition']
    search_fields = ['name', 'years']


@admin.register(HistoryMilestone)
class HistoryMilestoneAdmin(admin.ModelAdmin):
    list_display = ['year', 'title']
    list_filter = ['year']
    search_fields = ['title', 'description']