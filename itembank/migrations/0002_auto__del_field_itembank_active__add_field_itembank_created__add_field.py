# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Itembank.active'
        db.delete_column(u'itembank_itembank', 'active')

        # Adding field 'Itembank.created'
        db.add_column(u'itembank_itembank', 'created',
                      self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Itembank.modified'
        db.add_column(u'itembank_itembank', 'modified',
                      self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now),
                      keep_default=False)

        # Adding field 'Itembank.status'
        db.add_column(u'itembank_itembank', 'status',
                      self.gf('model_utils.fields.StatusField')(default='active', max_length=100, no_check_for_status=True),
                      keep_default=False)

        # Adding field 'Itembank.status_changed'
        db.add_column(u'itembank_itembank', 'status_changed',
                      self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor=u'status'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Itembank.active'
        db.add_column(u'itembank_itembank', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)

        # Deleting field 'Itembank.created'
        db.delete_column(u'itembank_itembank', 'created')

        # Deleting field 'Itembank.modified'
        db.delete_column(u'itembank_itembank', 'modified')

        # Deleting field 'Itembank.status'
        db.delete_column(u'itembank_itembank', 'status')

        # Deleting field 'Itembank.status_changed'
        db.delete_column(u'itembank_itembank', 'status_changed')


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
            'status': ('model_utils.fields.StatusField', [], {'default': "'active'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "u'status'"})
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