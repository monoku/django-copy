# -*- coding: utf-8 -*-
from django.db import models

#from datatrans.utils import register

class Copy(models.Model):
    key = models.SlugField(unique=True, editable=True)
    text = models.TextField()

    def __unicode__(self):
        return u'%s' % self.text

    class Meta:
        app_label = 'copy'

#class CopyTranslation(object):
    #fields = ('text',)

#register(Copy, CopyTranslation)