from django.contrib import admin
from .models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')
    list_filter = ('category',)
    ordering = ('category', 'title',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)

