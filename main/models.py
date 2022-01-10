import uuid

from django.db import models
from django.utils.text import slugify

from wiki.main import Wiki


class BaseIteratedModel(models.Model):
    use_default_description = False
    _main_field = None
    set_description_flag = True
    id = models.IntegerField(primary_key=True)
    main = models.CharField(max_length=30, null=True)
    slug = models.SlugField(unique=True, blank=True, default=uuid.uuid1)
    description = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return getattr(self, self._main_field)

    def save(self, *args, **kwargs):
        if not self._main_field:
            raise Exception('child model class must define the _main_field attribute')
        self.main = getattr(self, self._main_field)
        self.slug = slugify(self.main)
        if self.set_description_flag:
            self.set_description()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"{self.slug}/"

    def set_description(self):
        if not self.use_default_description:
            raise NotImplementedError('Child class with flag set_description_flag set to True must implement the '
                                      ' method')
        wiki = Wiki(self.main)
        self.description = wiki.obj.summary
