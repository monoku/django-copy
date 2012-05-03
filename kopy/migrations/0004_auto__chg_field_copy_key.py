# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Copy.key'
        db.alter_column('copy_copy', 'key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=500))


    def backwards(self, orm):
        
        # Changing field 'Copy.key'
        db.alter_column('copy_copy', 'key', self.gf('django.db.models.fields.CharField')(max_length=350, unique=True))


    models = {
        'kopy.copy': {
            'Meta': {'object_name': 'Copy', 'db_table': "'copy_copy'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'}),
            'text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['kopy']
