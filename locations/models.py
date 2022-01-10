from django.db import models

from main.models import BaseIteratedModel


class Country(BaseIteratedModel):
    use_default_description = True
    _main_field = 'name'
    name = models.CharField(max_length=20)
    region = models.CharField(max_length=10)
    surface_area = models.IntegerField("Surface Area of the country in km")
    population = models.IntegerField("Population")
    # density = models.IntegerField("Population density (per km2, 2017)")
    # sex_ratio = models.IntegerField("Sex ratio (m per 100 f, 2017)")
    # gdp = models.FloatField("GDP: Gross domestic product (million current US$)")
    # gdp_per_capita = models.FloatField("GDP per capita (current US$)")
