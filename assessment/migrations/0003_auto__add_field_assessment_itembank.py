# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Assessment.itembank'
        db.add_column(u'assessment_assessment', 'itembank',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['itembank.Itembank']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Assessment.itembank'
        db.delete_column(u'assessment_assessment', 'itembank_id')


    models = {
        u'assessment.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itembank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['itembank.Itembank']"}),
            'itemsneeded': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'itemsneededtopass': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'})
        },
        u'itembank.itembank': {
            'Meta': {'object_name': 'Itembank'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'})
        }
    }

    complete_apps = ['assessment']