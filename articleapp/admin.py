from django.contrib import admin

# Register your models here.
import articleapp
from articleapp.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('writer','project', 'title', 'image', 'content', 'created_at')