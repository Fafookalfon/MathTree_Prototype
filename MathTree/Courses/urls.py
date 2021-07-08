from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses.as_view(), name = "courses"),
    path('<str:course_name>/', views.course_view, name="course_view"),
    path('<str:course_name>/<int:chapter_index>/', views.chapter_view, name= "chapter_view"),
    path('<str:course_name>/<int:chapter_index>/<int:page_index>', views.page_view, name="page_view")
]