from django.urls import path

from .views import FileUploadView

app_name = "shareit"

urlpatterns = [
    path("", FileUploadView.as_view(), name="upload"),
]
