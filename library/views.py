#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json

from library.models import Book
from library.forms import SearchForm


def index(request):
    context = {
        "searchForm": SearchForm(),
    }
    return render(request, "library/index.html", context)


def book_search(request):
    search_by = request.GET.get("search_by", "Title")
    books = []
    current_path = request.get_full_path()

    keyword = request.GET.get("keyword", u"List")

    if keyword == u"List":
        books = Book.objects.all()
    else:
        if search_by == u"Title":
            keyword = request.GET.get("keyword", None)
            books = Book.objects.filter(title__contains=keyword).order_by("-title")[
                0:50
            ]
        elif search_by == u"ISBN":
            keyword = request.GET.get("keyword", None)
            books = Book.objects.filter(ISBN__contains=keyword).order_by("-title")[0:50]
        elif search_by == u"Author":
            keyword = request.GET.get("keyword", None)
            books = Book.objects.filter(author__contains=keyword).order_by("-title")[
                0:50
            ]

    paginator = Paginator(books, 5)
    page = request.GET.get("page", 1)

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    # ugly solution for &page=2&page=3&page=4
    if "&page" in current_path:
        current_path = current_path.split("&page")[0]

    context = {
        "books": books,
        "search_by": search_by,
        "keyword": keyword,
        "current_path": current_path,
        "searchForm": SearchForm(),
    }
    return render(request, "library/search.html", context)


def book_detail(request):
    ISBN = request.GET.get("ISBN", None)
    print(ISBN)
    if not ISBN:
        return HttpResponse("there is no such an ISBN")
    try:
        book = Book.objects.get(pk=ISBN)
    except Book.DoesNotExist:
        return HttpResponse("there is no such an ISBN")

    state = ""
    context = {
        "state": state,
        "book": book,
    }
    return render(request, "library/book_detail.html", context)


def about(request):
    return render(request, "library/about.html", {})
