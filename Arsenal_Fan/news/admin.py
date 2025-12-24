from django.contrib import admin
from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'is_published', 'comments_count']
    list_filter = ['date_created', 'is_published']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    readonly_fields = ['date_created']
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'content', 'image')
        }),
        ('Настройки', {
            'fields': ('is_published', 'date_created')
        }),
    )

    def comments_count(self, obj):
        return obj.comments.count()

    comments_count.short_description = 'Комментарии'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'news', 'created_at', 'text_preview']
    list_filter = ['created_at', 'news']
    search_fields = ['text', 'author__username', 'news__title']
    readonly_fields = ['created_at']

    def text_preview(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text

    text_preview.short_description = 'Текст (превью)'