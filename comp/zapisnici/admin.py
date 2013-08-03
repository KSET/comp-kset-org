from django.contrib import admin
from zapisnici.models import Zapisnik

class ZapisnikAdmin(admin.ModelAdmin):
    fields = ['zap_date', 'zap_sadrzaj', 'prisutni']
    list_display = ('zap_date', 'zap_sadrzaj')

admin.site.register(Zapisnik, ZapisnikAdmin)

