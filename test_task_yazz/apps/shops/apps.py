from contextlib import suppress

from django.apps import AppConfig


class ShopsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "shops"

    def ready(self):
        with suppress(ImportError):
            from shops import (  # noqa: F401 pylint: disable=import-outside-toplevel
                signals,
            )
