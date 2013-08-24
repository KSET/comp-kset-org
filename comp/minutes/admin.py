from django.contrib import admin
from minutes.models import Minutes 

from django.db import models
from tinymce.widgets import TinyMCE

from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.conf import settings

class MinutesAdmin(admin.ModelAdmin):
    fields = ('date', 'content', 'members_present', 'mail_notification')
    list_display = ('date', 'members_present', 'content')
    formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('mail_notification',) + self.readonly_fields
        return self.readonly_fields

    def save_model(self, request, obj, form, change):
        if not change:
            obj.slug = 'zapisnik-' + obj.date.strftime('%d-%m-%Y')
        super(MinutesAdmin, self).save_model(request, obj, form, change)



admin.site.register(Minutes, MinutesAdmin)

