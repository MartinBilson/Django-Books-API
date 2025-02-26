from django.urls import path
from .views import BookListCreateView, BookDetailView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet


# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')  # ✅ This registers 'book-list'


urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/', include(router.urls)),
]
