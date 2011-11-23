# -*- coding: utf-8 -*-

import logging

from django import template
from django.template import Variable
from django.template.loader import render_to_string
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import linebreaksbr

from kopy.models import Copy

register = template.Library()

def split_args(args):
    #TODO hacer mejor y mover:
    #los parametros son posicionales
    # los opt returnan un diccionario
    tag = ''
    opts = []
    kwargs = {}
    tag = args[0]
    for arg in args[1:]:
        if '=' in arg:
            opt, value = arg.split('=')
            opt = str(opt)
            if value[0]==value[-1] and (value[0]=="'" or value[0]=='"'):
                kwargs[opt] = value[1:-1]
            elif value=='True':
                kwargs[opt] = True
            elif value=='False':
                kwargs[opt] = False
            else:
                kwargs[opt] = value
        else:
            if arg[0]==arg[-1] and (arg[0]=="'" or arg[0]=='"'):
                arg = arg[1:-1]
            opts.append(arg)
    return tag, opts, kwargs


class CopyNode(template.Node):

    def __init__(self, copy, **kwargs):
        self.br = None
        if 'br' in kwargs:
            self.br = True
        self.is_variable = kwargs.get('is_variable', False)
        if self.is_variable:
            self.copy = template.Variable(copy)
        else:
            self.copy = copy

    def render(self, context):
        try:
            if self.is_variable:
                copy = self.copy.resolve(context)
            else:
                copy = self.copy
            try:
                if self.br:
                    return linebreaksbr(Copy.objects.get(key=copy).text)
                return Copy.objects.get(key=copy).text
            except ObjectDoesNotExist:
                return "The key '%s' doesn't exists in the database, please add it!" % copy
                
        except template.VariableDoesNotExist:
            return ''

@register.tag
def copy(parser, token):
    args = token.split_contents()
    tag, opts, kwargs = split_args(args)
    return CopyNode(*opts,**kwargs)