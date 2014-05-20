# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Assessment.status'
        db.add_column(u'assessment_assessment', 'status',
                      self.gf('model_utils.fields.StatusField')(default='active', max_length=100, no_check_for_status=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Assessment.status'
        db.delete_column(u'assessment_assessment', 'status')


    models = {
        u'assessment.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemsneeded': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'itemsneededtopass': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'})
        }
    }

    complete_apps = ['assessment']