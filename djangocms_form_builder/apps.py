from importlib import import_module

from django.apps import AppConfig
from django.conf import settings
from django.urls import NoReverseMatch, clear_url_caches, include, path, reverse
from django.utils.translation import gettext_lazy as _


class FormsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "djangocms_form_builder"
    verbose_name = _("Form builder")

    def ready(self):
        pass
