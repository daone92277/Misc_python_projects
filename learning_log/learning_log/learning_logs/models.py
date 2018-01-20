# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text= models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """return a string representation of the model"""
        return self.text
        return self.date_added

class Entry(models.Model):
    """something specific learned about a topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):

        """Return a string rpresentation of the model"""
        if len(self.text) >= 50:
            return self.text[:100] + "... continued"
        
        else:
            return self.text


