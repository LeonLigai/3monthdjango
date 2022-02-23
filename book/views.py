from django.shortcuts import render
from . import models, forms
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, reverse, redirect
from django.views import generic

class BookListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.book.objects.all

    def get_queryset(self):
        return self.queryset
class BookDetailView(generic.DetailView):
    template_name = "book_detail.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.book, id =book_id)

class BookCreateView(generic.CreateView):
    template_name = "add_book.html"
    form_class = forms.BookForm
    queryset = models.book.objects.all()
    success_url = "/book/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookCreateView, self).form_valid(form=form)

class BookUpdateView(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/book/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.book, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdateView, self).form_valid(form=form)

class BookDeleteView(generic.DeleteView):
    success_url = "/book/"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.book, id=book_id)


# def book_show_detail(request, id):
#     try:
#         book_show = get_object_or_404(models.book, id=id)
#         try:
#             comment = models.BookFeedBack.objects.filter(comment_id=id).\
#                 order_by("created_date")
#         except models.book:
#             print("No comments")
#     except models.book:
#         raise Http404("Book does not exist, try another id")
#     return render(request, 'book_detail.html', {"book_show" : book_show, "comment" : comment })

# def book_all(request):
#     book = models.book.objects.all()
#     return render(request, "book_list.html", {"book" : book})

# def add_book(request):
#     method = request.method
#     if method == "POST":
#         form = forms.BookShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("book:book_list"))
#             # return HttpResponse("Book Created Succesfully")
#     else:
#         form = forms.BookShowForm()
#     return render(request, "add_book.html", {"form" : form})

# def put_book_update(request, id):
#     book_id = get_object_or_404(models.book, id=id)
#     if request.method == "POST":
#         form = forms.BookShowForm(instance=book_id,
#                                   data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("book:book_list"))
#     else:
#         form = forms.BookShowForm(instance=book_id)
#     return render(request, "book_update.html", {"form": form,
#                                                 "book_book": book_id})
#
# def book_delete(request, id):
#     book_id = get_object_or_404(models.book, id=id)
#     book_id.delete()
#     return redirect(reverse("book:book_list"))