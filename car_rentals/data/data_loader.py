import django
from django.db import IntegrityError


def populate_db():
    from car_rentals.models import Manufacturer, Car
    Manufacturer.objects.all().delete()
    manufacturer = Manufacturer(name='Ferrari')
    manufacturer.save()

    Car.objects.create(make=manufacturer, model='430')


def run():
    django.setup()
    populate_db()


run()