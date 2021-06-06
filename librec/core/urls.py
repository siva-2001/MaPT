from django.urls import path

import core.views as view

urlpatterns = [
    path('books/', view.BookListView.as_view(), name="books"),
    path('books/<int:pk>/', view.BookDetail.as_view(), name="book"),
    path('contact/', view.Contact.as_view(), name="contact")
]