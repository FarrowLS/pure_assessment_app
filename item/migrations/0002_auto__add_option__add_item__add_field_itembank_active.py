# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Option'
        db.create_table(u'item_option', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.Item'])),
            ('option_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'item', ['Option'])

        # Adding model 'Item'
        db.create_table(u'item_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itembank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['item.Itembank'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('stem_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'item', ['Item'])

        # Adding field 'Itembank.active'
        db.add_column(u'item_itembank', 'active',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Option'
        db.delete_table(u'item_option')

        # Deleting model 'Item'
        db.delete_table(u'item_item')

        # Deleting field 'Itembank.active'
        db.delete_column(u'item_itembank', 'active')


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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['item.Item']"}),
            'option_text': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['item']