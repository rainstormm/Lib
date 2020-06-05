#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

import uuid, os


def custom_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    return filename


class Reader(models.Model):
    class Meta:
        verbose_name = 'Reader'
        verbose_name_plural = 'Readers'

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Reader')
    name = models.CharField(max_length=16, unique=True, verbose_name='Name')
    phone = models.IntegerField(unique=True, verbose_name='Phone')
    max_borrowing = models.IntegerField(default=5, verbose_name='Max Borrowing')
    balance = models.FloatField(default=0.0, verbose_name='Balance')
    photo = models.ImageField(blank=True, upload_to=custom_path, verbose_name='Photo')

    STATUS_CHOICES = (
        (0, 'normal'),
        (-1, 'overdue')
    )
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,
    )

    def __str__(self):
        return self.name


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


class Borrowing(models.Model):
    class Meta:
        verbose_name = 'Borrow'
        verbose_name_plural = 'Borrow'

    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name='Reader')
    ISBN = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='ISBN')
    date_issued = models.DateField(verbose_name='Borrow Time')
    date_due_to_returned = models.DateField(verbose_name='Expected Return Date')
    date_returned = models.DateField(null=True, verbose_name='Return Date')
    amount_of_fine = models.FloatField(default=0.0, verbose_name='Fine')

    def __str__(self):
        return '{} borrows {}'.format(self.reader, self.ISBN)
