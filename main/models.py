import uuid

from django.db import models
from django.utils.text import slugify

from wiki.main import Wiki


class BaseIteratedModel(models.Model):
    _main_field = None
    use_default_description = False
    set_description_flag = True
    use_default_image = False
    set_image_flag = True
    image_search_keyword = ''
    wiki = None

    id = models.IntegerField(primary_key=True)
    main = models.CharField(max_length=30, null=True)
    slug = models.SlugField(unique=True, blank=True, default=uuid.uuid1)
    description = models.TextField(blank=True)
    img = models.ImageField(blank=True)

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
        # if self.set_image_flag:       SAVING IMAGE ERROR
        #     self.set_image()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return f"{self.slug}/"

    def get_wiki_obj(self):
        if not self.wiki:
            self.wiki = Wiki(self.main)
        return self.wiki

    def set_description(self):
        if not self.use_default_description:
            raise NotImplementedError('Child class with flag set_description_flag set to True must implement the '
                                      ' method')
        wiki = self.get_wiki_obj()
        self.description = wiki.obj.summary

    def set_image(self):
        if not self.use_default_image:
            raise NotImplementedError('Child class with flag use_default_image set to True must implement the '
                                      ' method')
        from bing_image_downloader import downloader

        a = downloader.download(f'{self.main} {self.image_search_keyword}', limit=1, output_dir='dataset', adult_filter_off=True, force_replace=False,
                            timeout=60, verbose=True)
        print(a)
