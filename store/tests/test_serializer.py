from unittest import TestCase

from store.models import Books
from store.serialiser import BooksSerializer


class TestSirializer(TestCase):
    def book_ok(self):
        book_1 = Books.objects.create(name='You', price=34)
        book_2 = Books.objects.create(name='We', price=55)
        data = BooksSerializer([book_1, book_2], many=True).data
        expected_data = [
            {
                'id': book_1.id,
                'name': 'You',
                'price': '34.00'
            },
            {
                'id': book_2.id,
                'name': 'We',
                'price': '55.00'
            }

        ]
        self.assertEqual(expected_data, data)
        print(data)
