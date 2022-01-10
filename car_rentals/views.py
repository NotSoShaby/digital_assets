from django.shortcuts import render
from django.template import Context
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateResponseMixin, TemplateView

from car_rentals.models import Manufacturer, Car
from locations.models import Country
from wiki.main import Wiki


class ManufacturerListView(ListView):
    model = Manufacturer


class ManufacturerDetailView(DetailView):
    model = Manufacturer


class TrailView(TemplateView):
    template_name = 'car_rentals/home.html'

class CarListView(ListView):
    model = Car


class CarDetailView(DetailView):
    model = Car

    def get(self, request, **kwargs):
        manufacturer = Manufacturer.objects.get(slug=kwargs['manufacturer_slug'])
        self.object = Car.objects.get(slug=kwargs['car_slug'])
        context = self.get_context_data()
        return self.render_to_response(context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AutomaticView(View):
    model_slug_mapping = {
        'manufacturer_slug': Manufacturer,
        'car_slug': Car,
        'country_slug': Country
    }

    def get(self, request, **kwargs):
        context = {}
        for slug_type, user_value in kwargs.items():
            model = self.model_slug_mapping[slug_type]
            obj = model.objects.get(slug=user_value)
            context[model.__qualname__.lower()] = obj

        context['title'] = ' '.join(kwargs.values())
        return render(request,'car_rentals/auto.html',context=context)
