# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Zapisnik'
        db.create_table(u'zapisnici_zapisnik', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zap_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('zap_sadrzaj', self.gf('django.db.models.fields.TextField')()),
            ('prisutni', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'zapisnici', ['Zapisnik'])


    def backwards(self, orm):
        # Deleting model 'Zapisnik'
        db.delete_table(u'zapisnici_zapisnik')


    models = {
        u'zapisnici.zapisnik': {
            'Meta': {'object_name': 'Zapisnik'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prisutni': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'zap_date': ('django.db.models.fields.DateTimeField', [], {}),
            'zap_sadrzaj': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['zapisnici']