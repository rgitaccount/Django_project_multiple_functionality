from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse
from . import models, forms


class ParserFormView(generic.FormView):
    template_name = "scrapy/parser.html"
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            return redirect(reverse("scrapy_url:parsed_results"))
        else:
            return super(ParserFormView, self).post(request, *args, **kwargs)


class ScrapedListView(generic.ListView):
    template_name = "scrapy/parsed_results.html"
    queryset = models.GoodReads.objects.order_by("id")
    paginate_by = 8





