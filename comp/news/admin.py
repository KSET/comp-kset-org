from news.models import News
from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
from django.conf import settings

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','body', 'date')
    fieldsets = (
        (None, { 'fields': ['title', 'slug', 'body']} ),
    )
    prepopulated_fields = {'slug': ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super(NewsAdmin, self).save_model(request, obj, form, change)

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }

admin.site.register(News, NewsAdmin)
