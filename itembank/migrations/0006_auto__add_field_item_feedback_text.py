# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Item.feedback_text'
        db.add_column(u'itembank_item', 'feedback_text',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Item.feedback_text'
        db.delete_column(u'itembank_item', 'feedback_text')


    models = {
        u'itembank.item': {
            'Meta': {'object_name': 'Item'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'feedback_text': ('django.db.models.fields.TextField', [], {'default': "''"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itembank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['itembank.Itembank']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'}),
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