from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponse
from django.template import loader

from .models import Book
from .forms import BookForm

def index(request):
	template = loader.get_template("index.html")
	return HttpResponse(template.render())

def books_list(request):
	all_books = Book.objects.all()
	context = {
		"books": all_books
	}
	
	return render(request, "index.html", context)

def add_book_view(request):
	if request.method == "POST":
		form = BookForm(request.POST)
		
		if form.is_valid():
			form.save()
			return redirect("index")
	
	else:
		form = BookForm
	
	return render(request, "add.html", {"form": form})
	
def search_results_view(request):
	query = request.GET.get("q")
	results = Book.objects.none()
	
	if (query):
		results = Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query) | Q(year__icontains=query))
	
	return render(request, "results.html", {"results": results, "query": query})
