# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Assessment.testee'
        db.delete_column(u'assessment_assessment', 'testee_id')


    def backwards(self, orm):
        # Adding field 'Assessment.testee'
        db.add_column(u'assessment_assessment', 'testee',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['auth.User'], unique=True),
                      keep_default=False)


    models = {
        u'assessment.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itembank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['itembank.Itembank']"}),
            'itemsneeded': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'itemsneededtopass': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"})
        },
        u'itembank.itembank': {
            'Meta': {'object_name': 'Itembank'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['assessment']