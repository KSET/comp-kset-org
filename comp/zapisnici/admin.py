from django.contrib import admin
from zapisnici.models import Zapisnik

from django.db import models
from tinymce.widgets import TinyMCE

from django.core.mail import EmailMessage
from django.conf import settings

class ZapisnikAdmin(admin.ModelAdmin):
    fields = ['zap_date', 'zap_sadrzaj', 'prisutni', 'mail_notifikacija']
    list_display = ('zap_date', 'zap_sadrzaj', 'mail_notifikacija')

    def save_model(self, request, obj, form, change):
        if obj.mail_notifikacija == True:
            subject, from_email, to = 'Zapisnik sa sastanka', settings.EMAIL_HOST_USER, 'sendto@mail.com'
            html_message = '<b>'+str(obj.zap_date)+'</b>'+'<p><b>Prisutni: </b></p>'+obj.prisutni+'<p> <b>Sadrzaj:</b> '+obj.zap_sadrzaj+'</p>'
            msg = EmailMessage(subject, html_message, from_email, [to])
            msg.content_subtype = "html"
            msg.send()

        super(ZapisnikAdmin, self).save_model(request, obj, form, change)


    formfield_overrides = {
            models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }

admin.site.register(Zapisnik, ZapisnikAdmin)

