from __future__ import unicode_literals

from django.db import models


class People(models.Model):
    name = models.CharField(max_length=30, db_index=True)

    def __unicode__(self):
        return self.name


class Document(models.Model):
    education = models.CharField(max_length=50, db_index=True)
    people_id = models.ForeignKey(People)

    def __unicode__(self):
        return '%s: %s' % (self.education, self.people_id.name)
