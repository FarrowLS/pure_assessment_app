# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Assessment'
        db.create_table(u'assessment_assessment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('itemsneeded', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'assessment', ['Assessment'])


    def backwards(self, orm):
        # Deleting model 'Assessment'
        db.delete_table(u'assessment_assessment')


    models = {
        u'assessment.assessment': {
            'Meta': {'object_name': 'Assessment'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'itemsneeded': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['assessment']