#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms


class SearchForm(forms.Form):
        CHOICES = [
            (u'ISBN', u'ISBN'),
            (u'Title', u'Title'),
            (u'Author', u'Author')
        ]

        search_by = forms.ChoiceField(
            label='',
            choices=CHOICES,
            widget=forms.RadioSelect(),
            initial=u'Title',
        )

        keyword = forms.CharField(
            label='',
            max_length=32,
            widget=forms.TextInput(attrs={
                'class': 'form-control input-lg',
                'placeholder': u'Enter the Information about the Book',
                'name': 'keyword',
            })
        )
