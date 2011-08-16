# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.fields import CharField
from django.contrib import admin
#from ckeditor.widgets import CKEditorWidget

from copy.models import Copy

class CopyAdminForm(ModelForm):
    #text = CharField(widget=CKEditorWidget())
    class Meta:
        model = Copy

class CopyAdmin(admin.ModelAdmin):
    list_display = ['key', 'text']
    ordering = ('key',)
    search_fields = ('text',)
    form = CopyAdminForm 

admin.site.register(Copy, CopyAdmin)