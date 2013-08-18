# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Zapisnik.mail_notifikacija'
        db.add_column(u'zapisnici_zapisnik', 'mail_notifikacija',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # Changing field 'Zapisnik.prisutni'
        db.alter_column(u'zapisnici_zapisnik', 'prisutni', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):
        # Deleting field 'Zapisnik.mail_notifikacija'
        db.delete_column(u'zapisnici_zapisnik', 'mail_notifikacija')


        # Changing field 'Zapisnik.prisutni'
        db.alter_column(u'zapisnici_zapisnik', 'prisutni', self.gf('django.db.models.fields.CharField')(max_length=200))

    models = {
        u'zapisnici.zapisnik': {
            'Meta': {'object_name': 'Zapisnik'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail_notifikacija': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prisutni': ('django.db.models.fields.TextField', [], {}),
            'zap_date': ('django.db.models.fields.DateTimeField', [], {}),
            'zap_sadrzaj': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['zapisnici']