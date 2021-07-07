from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses, name = "courses"),
    path('sigmatest', views.sigmatest, name="sigmatest")
]