#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models

import uuid, os


def custom_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return filename


class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    ISBN = models.CharField(max_length=13, primary_key=True, verbose_name='ISBN')
    title = models.CharField(max_length=128, verbose_name='Title')
    author = models.CharField(max_length=32, verbose_name='Author')
    press = models.CharField(max_length=64, verbose_name='Press')

    description = models.CharField(max_length=1024, default='', verbose_name='Description')
    price = models.CharField(max_length=20, null=True, verbose_name='Price')

    category = models.CharField(max_length=64, default=u'Literature', verbose_name='Category')
    cover = models.ImageField(blank=True, upload_to=custom_path, verbose_name='Cover')
    index = models.CharField(max_length=16, null=True, verbose_name='Index')
    location = models.CharField(max_length=64, default=u'first floor', verbose_name='Location')
    quantity = models.IntegerField(default=1, verbose_name='Quantity')

    def __str__(self):
        return self.title + self.author


