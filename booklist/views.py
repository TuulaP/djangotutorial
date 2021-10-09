from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from booklist.models import Book, Location, Comment
from .forms import CommentForm


def book_index(request):

    books = Book.objects.all().order_by('-created_on')

    context = {
        "books": books,
    }

    return render(request, "book_index.html", context)


def book_category(request, category):

    books = Book.objects.filter(

        categories__name__contains=category

    ).order_by(
        '-created_on'
    )

    context = {
        "category": category,
        "books": books

    }

    return render(request, "book_category.html", context)


def book_location(request, location):

    books = Book.objects.filter(

        locations__name__contains=location

    ).order_by(
        '-created_on'
    )

    context = {
        "location": location,
        "books": books

    }

    return render(request, "book_location.html", context)




def book_detail(request, pk):

    book = Book.objects.get(pk=pk)

    form = CommentForm()

    if request.method == 'POST':

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = Comment(

                author=form.cleaned_data["author"],

                body=form.cleaned_data["body"],

                book=book

            )

            comment.save()


    comments = Comment.objects.filter(book=book)

    context = {

        "book": book,

        "comments": comments,

        "form": form,

    }

    return render(request, "book_detail.html", context)


