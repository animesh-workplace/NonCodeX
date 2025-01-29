from django.db import connection
from django.apps import AppConfig


class QueryEngineConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "query_engine"

    def ready(self):
        """Optimize SQLite performance when Django starts."""
        with connection.cursor() as cursor:
            cursor.execute("PRAGMA cache_size=-1000000;")  # Increase cache
            cursor.execute("PRAGMA synchronous=OFF;")  # Speed up writes
            cursor.execute("PRAGMA journal_mode=WAL;")  # Improve concurrency
            cursor.execute(
                "PRAGMA temp_store=MEMORY;"
            )  # Use memory for temporary tables
