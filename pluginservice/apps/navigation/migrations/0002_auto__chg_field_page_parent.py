# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.parent'
        db.alter_column(u'navigation_page', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['navigation.Page'], null=True))

    def backwards(self, orm):

        # Changing field 'Page.parent'
        db.alter_column(u'navigation_page', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(default=3, to=orm['navigation.Page']))

    models = {
        u'navigation.page': {
            'Meta': {'object_name': 'Page'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['navigation.Page']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['navigation']