from django.contrib import admin
from library.models import Book, Borrowing, Reader

admin.site.register(Book)
admin.site.register(Borrowing)
admin.site.register(Reader)

admin.site.name = 'Library Management System'
admin.site.site_header = 'Library Management System'
