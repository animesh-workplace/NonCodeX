from django.urls import path
from .views import ChromosomeRegionUploadView

urlpatterns = [
    path("data/", ChromosomeRegionUploadView.as_view(), name="query-data"),
]
