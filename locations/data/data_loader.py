import django
import pandas as pd
import regex as re


def populate_countries():
    from locations.models import Country
    Country.objects.all().delete()
    new_col_names = ['name', 'region', 'surface_area', 'population']
    df = pd.read_csv('locations/data/country_profile_variables.csv', header=None, skiprows=1, usecols=new_col_names, names=new_col_names)
    # the population is in thousands
    df['population'] = df['population'].multiply(1000)
    df['region'] = df['region'].apply(lambda x: ' '.join(re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', x)))
    df['surface_area'] = df['surface_area'].apply(lambda x: 0 if x == '~0' else x)
    df_records = df.to_dict('records')

    model_instances = [Country(
        name=record['name'],
        region=record['region'],
        surface_area=record['surface_area'],
        population=record['population'],
    ) for record in df_records]

    for obj in model_instances:
        obj.save()


def run():
    django.setup()
    populate_countries()


run()