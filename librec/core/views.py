from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.http import HttpResponseRedirect

import core.models as models


class BookListView(ListView):

    model = models.Book
    paginate_by = 7
    template_name = "book_list.html"


class BookDetail(View):
    def get(self, request, pk):
        book = models.Book.objects.get(id=pk)
        reviews = models.Review.objects.filter(book=book)
        ctx = {
            "book": book,
            "reviews": reviews
        }
        return render(request, "book.html", context=ctx)

    def post(self, request, pk):
        user = request.user
        text = request.POST['review__text']
        book = models.Book.objects.get(id=pk)

        review = models.Review(
            user=user,
            text=text,
            book=book
        )
        review.save()

        return HttpResponseRedirect(request.path_info)


class Contact(View):
    def post(self, request):
        user = request.user
        text = request.POST['review__text']

        contact = models.Contact(
            user=user,
            text=text
        )
        contact.save()

        return redirect('../books/')





