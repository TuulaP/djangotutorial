from django.urls import path
from . import views

urlpatterns = [
    path("", views.book_index, name="book_index"),
    path("<int:pk>/", views.book_detail, name="book_detail"),
    path("<category>/", views.book_category, name="book_category"),
    path("<location>/", views.book_location, name="book_location"),

]


