from django.db import models
from main.models import BaseIteratedModel
from wiki.main import Wiki


class Manufacturer(BaseIteratedModel):
    use_default_description = True
    _main_field = 'name'
    name = models.CharField(max_length=20)


class Car(BaseIteratedModel):
    _main_field = 'model'
    make = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    model = models.CharField(max_length=30)

    def set_description(self):
        wiki = Wiki(f'{self.make.main} {self.main}')
        self.description = wiki.obj.summary

