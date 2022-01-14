from django.urls import path, include, re_path

from car_rentals.views import ManufacturerListView, ManufacturerDetailView, CarListView, CarDetailView, \
    AutomaticView, TrailView

urlpatterns = [
    path('', TrailView.as_view(), name='dfgfd'),
    # path('', ManufacturerListView.as_view(), name='manufacturer_list'),
    # path('<slug:slug>', ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    #
    # path('cars', CarListView.as_view(), name='car_list'),
    # path('<slug:manufacturer_slug>-cars-<slug:car_slug>/', CarDetailView.as_view(), name='car_detail'),
    re_path('^(?:/(?P<manufacturer_slug>[a-zA-Z]+)|)(?:/(?P<car_slug>[a-zA-Z]+)|)(?:/(?P<country_slug>[a-zA-Z]+))?/$',
            AutomaticView.as_view(), name='trial'),
]
