from django.urls import path

from book.views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("", BookListCreateAPIView.as_view(), name="book_list"),
    path("<int:pk>/", BookRetrieveUpdateDestroyAPIView.as_view(), name="book_detail")
]
