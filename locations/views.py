from django.views.generic import ListView, DetailView

from locations.models import Country


class CountryListView(ListView):
    model = Country


class CountryDetailView(DetailView):
    model = Country
