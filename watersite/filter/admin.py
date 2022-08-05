from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *




class FilterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'get_html_photo', 'is_published', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'get_html_photo')  # поля которые не редактируются в админ панели
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=80>")    # Это отображает миниатюру фото в админ панели

    get_html_photo.short_description = "Preview"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}   ## этот слаг автоматически вводит url адрес на англязык для домена

admin.site.register(Filter, FilterAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_title = 'Admin panel'   # Изменение в названии заголовка админ панели
admin.site.site_header = 'Admin panel'