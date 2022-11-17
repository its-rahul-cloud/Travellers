from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import app.signals