import django
import pandas as pd
import boto3
import io

from django.conf import settings


def populate_db():
    from car_rentals.models import Manufacturer, Car
    Manufacturer.objects.all().delete()
    manufacturer = Manufacturer(name='Ferrari')
    manufacturer.save()

    Car.objects.create(make=manufacturer, model='430')


def run():
    django.setup()
    populate_db()


# django.setup()
# s3 = boto3.client('s3')
# obj = s3.get_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME, Key='data/cars_makers_table.csv')
# df = pd.read_csv(io.BytesIO(obj['Body'].read()))
run()