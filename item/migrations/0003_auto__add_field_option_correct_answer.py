# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Option.correct_answer'
        db.add_column(u'item_option', 'correct_answer',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Option.correct_answer'
        db.delete_column(u'item_option', 'correct_answer')


    models = {
        u'item.item': {
            'Meta': {'object_name': 'Item'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itembank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.Itembank']"}),
            'stem_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'item.itembank': {
            'Meta': {'object_name': 'Itembank'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'item.option': {
            'Meta': {'object_name': 'Option'},
            'correct_answer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.Item']"}),
            'option_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['item']