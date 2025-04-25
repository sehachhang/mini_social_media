from django.apps import AppConfig

class MiniSocialmediaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mini_socialmedia'

    def ready(self):
        import mini_socialmedia.signals 

def ready(self):
    import mini_socialmedia.signals
