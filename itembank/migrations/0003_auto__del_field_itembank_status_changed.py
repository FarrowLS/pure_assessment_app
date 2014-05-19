# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Itembank.status_changed'
        db.delete_column(u'itembank_itembank', 'status_changed')


    def backwards(self, orm):
        # Adding field 'Itembank.status_changed'
        db.add_column(u'itembank_itembank', 'status_changed',
                      self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor=u'status'),
                      keep_default=False)


    models = {
        u'itembank.item': {
            'Meta': {'object_name': 'Item'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itembank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['itembank.Itembank']"}),
            'stem_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'itembank.itembank': {
            'Meta': {'object_name': 'Itembank'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'})
        },
        u'itembank.option': {
            'Meta': {'object_name': 'Option'},
            'correct_answer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['itembank.Item']"}),
            'option_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['itembank']