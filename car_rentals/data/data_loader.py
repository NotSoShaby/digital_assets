import django
from django.db import IntegrityError


def populate_db():
    from car_rentals.models import Manufacturer, Car
    try:
        manufacturer = Manufacturer(name='Ferrari')
        manufacturer.save()
    except IntegrityError:
        manufacturer = Manufacturer.objects.get(slug='ferrari')

    Car.objects.create(make=manufacturer, model='430')


def run():
    django.setup()
    populate_db()


run()