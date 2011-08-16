# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Copy'
        db.create_table('copy_copy', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50, db_index=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('copy', ['Copy'])

        # Adding model 'CopyTranslation'
        db.create_table('copy_copytranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('copy', ['CopyTranslation'])


    def backwards(self, orm):
        
        # Deleting model 'Copy'
        db.delete_table('copy_copy')

        # Deleting model 'CopyTranslation'
        db.delete_table('copy_copytranslation')


    models = {
        'copy.copy': {
            'Meta': {'object_name': 'Copy'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'copy.copytranslation': {
            'Meta': {'object_name': 'CopyTranslation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['copy']
