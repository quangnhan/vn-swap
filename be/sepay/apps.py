from django.apps import AppConfig


class SepayConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sepay'

    def ready(self) -> None:
        import sepay.signals