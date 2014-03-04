# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table(u'scorecard_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('score', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'scorecard', ['Player'])


    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table(u'scorecard_player')


    models = {
        u'scorecard.player': {
            'Meta': {'object_name': 'Player'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'score': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['scorecard']