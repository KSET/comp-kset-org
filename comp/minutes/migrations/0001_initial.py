# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Minutes'
        db.create_table(u'minutes_minutes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('members_present', self.gf('django.db.models.fields.TextField')()),
            ('mail_notification', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'minutes', ['Minutes'])


    def backwards(self, orm):
        # Deleting model 'Minutes'
        db.delete_table(u'minutes_minutes')


    models = {
        u'minutes.minutes': {
            'Meta': {'object_name': 'Minutes'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mail_notification': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'members_present': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['minutes']