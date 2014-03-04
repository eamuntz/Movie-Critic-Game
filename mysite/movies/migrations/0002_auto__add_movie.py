# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'movies_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('year', self.gf('django.db.models.fields.DateTimeField')()),
            ('mpaa_rating', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('critic_score', self.gf('django.db.models.fields.IntegerField')()),
            ('synopsis', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('poster', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('runtime', self.gf('django.db.models.fields.IntegerField')()),
            ('director', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'movies', ['Movie'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'movies_movie')


    models = {
        u'movies.movie': {
            'Meta': {'object_name': 'Movie'},
            'critic_score': ('django.db.models.fields.IntegerField', [], {}),
            'director': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpaa_rating': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'poster': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {}),
            'synopsis': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'year': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['movies']