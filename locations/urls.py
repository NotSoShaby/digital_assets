from django.urls import path
from locations.views import CountryListView, CountryDetailView

urlpatterns = [
    path('countries/', CountryListView.as_view(), name='country_list'),
    path('countries/<slug:slug>/', CountryDetailView.as_view(), name='country_detail'),
]