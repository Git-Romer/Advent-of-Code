from django.apps import AppConfig
from django.conf import settings
import socket

class ScoreboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scoreboard'
    
    def ready(self):
        if settings.DEBUG:
            print(f"Server launched on {socket.gethostbyname(socket.gethostname())} and Debug mode is on\nReocurring scoreboard update will not be executed!")
        else:
            from scoreboard_updater import updater
            updater.start()