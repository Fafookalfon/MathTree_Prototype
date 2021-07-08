from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses.as_view(), name = "courses"),
]