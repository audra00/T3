from django.urls import path
from . import views

urlpatterns = [
	path("", views.books_list, name="index"),
	path("add/", views.add_book_view, name="add_book"),
	path("results/", views.search_results_view, name="results")
]
