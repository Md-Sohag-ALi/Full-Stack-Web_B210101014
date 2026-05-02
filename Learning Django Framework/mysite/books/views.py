from django.shortcuts import render
from .models import Book
from django.views.generic import ListView,CreateView,UpdateView,DeleteView #class based view er jonno lage
from django.urls import reverse_lazy
from django.contrib import messages 
# Create your views here.
"""before we learned function based view """
def home(request):
    books = Book.objects.all() #model
    return render(render, '' , {'books' : books}) #template name ,sending data

""" Now class based view """
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'
 

#CREATE
class BookCreateView(CreateView):
    model = Book
    fields =['title','author']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list') #redirect() er poriborte eta use hoi 
                                            #book create hower pore book-list page a niye jabe
    
    def form_valid(self, form):
        messages.success(self.request, 'Book Created Successfully!')
        return super().form_valid(form) 
    
class BookUpdateView(UpdateView):
    model = Book
    fields =['title','author']
    template_name = 'books/book_update.html'
    success_url = reverse_lazy('book-list') #redirect() er poriborte eta use hoi 
                                            #book create hower pore book-list page a niye jabe
    
    def form_valid(self, form):
        messages.success(self.request, 'Book Updated Successfully!')
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    model = Book
    fields =['title','author']
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book-list') #redirect() er poriborte eta use hoi 
                                            #book create hower pore book-list page a niye jabe
    
    def form_valid(self, form):
        messages.success(self.request, 'Book Deleted Successfully!')
        return super().form_valid(form)    