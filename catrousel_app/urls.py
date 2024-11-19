from django.urls import path

from . import views

app_name = "catrousel_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("download/<str:cat_id>", views.download_cat, name="download"),
]
