from django.apps import AppConfig


class BillofmaterialConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.billofmaterial'

    def ready(self):
        import apps.billofmaterial.signals
