# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Itembank'
        db.create_table(u'itembank_itembank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'itembank', ['Itembank'])

        # Adding model 'Item'
        db.create_table(u'itembank_item', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('itembank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['itembank.Itembank'])),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('stem_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'itembank', ['Item'])

        # Adding model 'Option'
        db.create_table(u'itembank_option', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['itembank.Item'])),
            ('option_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correct_answer', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'itembank', ['Option'])


    def backwards(self, orm):
        # Deleting model 'Itembank'
        db.delete_table(u'itembank_itembank')

        # Deleting model 'Item'
        db.delete_table(u'itembank_item')

        # Deleting model 'Option'
        db.delete_table(u'itembank_option')


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
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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