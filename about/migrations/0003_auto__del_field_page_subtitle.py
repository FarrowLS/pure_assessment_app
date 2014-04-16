# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.subtitle'
        db.delete_column(u'about_page', 'subtitle')


    def backwards(self, orm):
        # Adding field 'Page.subtitle'
        db.add_column(u'about_page', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500),
                      keep_default=False)


    models = {
        u'about.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        }
    }

    complete_apps = ['about']