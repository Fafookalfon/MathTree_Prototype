from django.urls import path
from . import views


urlpatterns = [
    path('', views.courses.as_view(), name = "courses"),
    path('<str:course_name>/', views.course_view, name="course_view"),
    path('<str:course_name>/<int:chapter_index>/', views.chapter_view, name= "chapter_view"),
    path('<str:course_name>/<int:chapter_index>/<int:page_index>', views.page_view, name="page_view"),
    path('<str:course_name>/<int:chapter_index>/<int:page_index>/comment', views.page_comment_view, name="page_comment_view"),
    path('general_tree_view', views.general_tree_view, name="general_tree_view"),
    path('<str:course_name>/<int:chapter_index>/exercises_view', views.exercises_view, name="exercises_view"),
    path('<str:course_name>/<int:chapter_index>/<int:page_index>/send_comment/<int:solution>', views.send_comment, name="send_comment"),
    path('general_tree_view/tree_course/<str:course_name>', views.tree_course_view, name="tree_course_view"),
    path('general_tree_view/tree_prerequisite/<str:prerequisite_name>/<str:target_name>', views.tree_prerequisite_view, name="tree_prerequisite_view"),
    path('general_tree_view/tree_home_view', views.tree_home_view, name="tree_home_view")
    
]