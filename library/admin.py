from django.contrib import admin
from library.models import Book

admin.site.register(Book)

admin.site.name = "Library Management System"
admin.site.site_header = "Library Management System"
