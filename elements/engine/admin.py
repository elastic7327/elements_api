from django.contrib import admin

from engine.models import Csv, Content


class CsvAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'file', 'is_archived')
    search_fields = ['date', ]


class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ['title', ]


admin.site.register(Csv, CsvAdmin)
admin.site.register(Content, ContentAdmin)
