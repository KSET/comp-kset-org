from django.db import models
from tinymce.widgets import TinyMCE

class Zapisnik(models.Model):
    zap_date = models.DateTimeField('datum zapisnika')
    zap_sadrzaj = models.TextField('sadrzaj zapisnika')
    prisutni = models.TextField('prisutni')

    def __unicode__(self):
        return self.zap_sadrzaj # Promijeniti u nesto pametnije

    class Meta:
        verbose_name_plural = "zapisnici"

