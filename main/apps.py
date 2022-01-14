import django
from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        all_models = django.apps.apps.get_models()
        all_models = [m for m in all_models if m.__qualname__ != 'BaseIteratedModel']
        for model in all_models:
            if getattr(model, 'iter_field', False):
                model.generate_all_urls()
