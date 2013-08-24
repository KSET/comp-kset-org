# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Minutes.slug'
        db.add_column(u'minutes_minutes', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default=-1, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Minutes.slug'
        db.delete_column(u'minutes_minutes', 'slug')


    models = {
        u'minutes.minutes': {
            'Meta': {'object_name': 'Minutes'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_present': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['minutes']