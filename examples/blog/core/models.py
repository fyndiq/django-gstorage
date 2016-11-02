from __future__ import unicode_literals

from django.db import models


class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    cover = models.ImageField()
    created = models.DateTimeField(auto_add_now=True)
    updated = models.DateTimeField(auto_add_now=True)

    def __unicode__(self):
        return self.title
