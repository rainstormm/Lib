from django.test import TestCase
from library.models import Book

# Create your tests here.
class IndexPageTest(TestCase):
    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        # self.assertTemplateUsed(response,'index.html')
        self.assertTemplateUsed(template_name='index.html')

class BookSearchPageTest(TestCase):

    def test_search_page(self):
        response = self.client.get('/search/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(template_name='search.html')



class BookDetailPageTest(TestCase):
    def setUp(self) -> None:
        Book.objects.create(ISBN="11111111",title="title1",author="author1",press="press1",quantity=5)
    def test_ISBN(self):
        book=Book.objects.get(ISBN="11111111")
        self.assertEqual(book.ISBN, '11111111')

    def test_detail_page(self):
        response = self.client.get('/book/detail')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(template_name='book_detail.html')

class AboutPageTest(TestCase):
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(template_name='about.html')