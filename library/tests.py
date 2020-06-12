from django.test import TestCase
from library.models import Book


# Create your tests here.
class IndexPageTest(TestCase):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(template_name='index.html')

class BookSearchPageTest(TestCase):
    def setUp(self) -> None:
        Book.objects.create(ISBN="11111111",title="title1",author="author1",press="press1",quantity=5)

    def test_search(self):
         # url=reversed('library:book_search')
         # response = self.client.post(url,data={"search_by":"Title","keyword":"title1"})
         # self.assertEqual(response.context['keyword'],b"Title")
        response = self.client.get('/search/?search_by=Title&keyword=title1')
        self.assertEqual(response.context['search_by'], "Title")
        self.assertEqual(response.context['keyword'], "title1")
        response = self.client.get('/search/?search_by=ISBN&keyword=11111111')
        self.assertEqual(response.context['search_by'], "ISBN")
        self.assertEqual(response.context['keyword'], "11111111")
        response = self.client.get('/search/?search_by=Author&keyword=author1')
        self.assertEqual(response.context['search_by'], "Author")
        self.assertEqual(response.context['keyword'], "author1")

    def test_paginator(self):
        response = self.client.get('/search/?search_by=Author&keyword=author1&page=3.5')
        self.assertEquals(response.context['books'].number, 1)
        response = self.client.get('/search/?search_by=Author&keyword=author1&page=3')
        self.assertEquals(response.context['books'].number, 1)

    def test_search_page(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(template_name='search.html')


class BookDetailPageTest(TestCase):
    def setUp(self) -> None:
        Book.objects.create(ISBN="11111111",title="title1",author="author1",press="press1",quantity=5)
    def test_ISBN(self):
        book=Book.objects.get(ISBN="11111111")
        self.assertEqual(book.title, 'title1')
        self.assertEqual(book.author, 'author1')
        self.assertEqual(book.quantity, 5)
        response = self.client.get('/book/detail?ISBN=11111111')
        self.assertEqual(response.context['book'], book )
    def test_no_ISBN(self):
        response = self.client.get('/book/detail?ISBN=None')
        self.assertEqual(response.content, b'there is no such an ISBN')
        response = self.client.get('/book/detail?ISBN=22222222')
        self.assertEqual(response.content, b'there is no such an ISBN')
    def test_detail_page(self):
        response = self.client.get('/book/detail')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(template_name='book_detail.html')


class AboutPageTest(TestCase):
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(template_name='about.html')