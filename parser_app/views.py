from django.shortcuts import render
from django.shortcuts import redirect,HttpResponse, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView,FormView,DetailView
from . import parser, models , forms


class ParserFormView(FormView):
    template_name = "parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            # return HttpResponse("Parser Success")
            return redirect(reverse('parser:film_list'))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)

class FilmListView(ListView):
    template_name = 'film.html'
    queryset = models.Film.objects.all()

    def get_queryset(self):
        return self.queryset

class FilmDetailView(DetailView):
    template_name = "film_detail.html"

    def get_object(self, **kwargs):
        film_id = self.kwargs.get("id")
        return get_object_or_404(models.Film, id =film_id)