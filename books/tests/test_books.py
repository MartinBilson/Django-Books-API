from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from books.models import Book
from django.urls import reverse

class BookAPITestCase(APITestCase):  
    def setUp(self):
        self.book = Book.objects.create(
            title="Harry Potter",
            author="J.K. Rowling",
            publication_date="1997-06-26",
            isbn="9780747532743",
            summary="A young wizard's journey begins."
        )

    def test_get_all_books(self):
        url = reverse('book-list')  # ✅ Make sure 'book-list' exists in your router
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
