from django.urls import path
from . import views


urlpatterns = [
    path('', views.SendComment, name="comments")
]