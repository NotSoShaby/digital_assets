from django.urls import path, include, re_path


from car_rentals.views import *
urlpatterns = [
    # path('', TrailView.as_view(), name='dfgfd'),
    # path('', ManufacturerListView.as_view(), name='manufacturer_list'),
    # path('<slug:slug>', ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    #
    # path('cars', CarListView.as_view(), name='car_list'),
    # path('<slug:manufacturer_slug>-cars-<slug:car_slug>/', CarDetailView.as_view(), name='car_detail'),
    path('carslist/', carList, name="carlist"),
    path('description/<int:id>/', description, name="description"),
    re_path(r'(?P<manufacturer_slug>[a-zA-Z]+)/(?P<car_slug>[0-9]+)/(?P<country_slug>[a-zA-Z]+)/$',
            AutomaticView.as_view(), name='trial'),
]
