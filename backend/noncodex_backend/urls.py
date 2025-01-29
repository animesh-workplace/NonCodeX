import os
from dotenv import load_dotenv
from django.contrib import admin
from django.conf import settings
from django.urls import path, include

load_dotenv(settings.BASE_DIR / ".env")

admin.site.site_title = "NonCodeX"
admin.site.index_title = "NonCodeX Admin Panel"
admin.site.site_header = "[ NonCodeX Admin Panel ]"

urlpatterns = [
    path(
        f"{os.getenv('BASE_URL')}",
        include(
            [
                path("admin/", admin.site.urls),
                path(
                    "api/",
                    include(
                        [
                            path("query/", include("query_engine.urls")),
                        ]
                    ),
                ),
            ]
        ),
    )
]
