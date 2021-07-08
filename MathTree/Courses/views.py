from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Course, Chapter, ChapterPage

class courses(ListView) : 

    template_name = 'Courses/courses.html'
    context_object_name = 'Courses_list'

    def get_queryset(self) : 
        return Course.objects.all()


def course_view(request, course_name) :

    course = Course.objects.filter(name=course_name).first()
    return render(request, 'Courses/course_view.html', {"course" : course})

def chapter_view(request, course_name, chapter_index) : 
    
    chapter = Chapter.objects.filter( course__name=course_name, index=chapter_index).first()
    return render(request, 'Courses/chapter_view.html', {"chapter" : chapter})

def page_view(request, course_name, chapter_index, page_index) : 

    page = ChapterPage.objects.filter(chapter__course__name=course_name, chapter__index=chapter_index, index=page_index).first()
    return render(request, 'Courses/page_view.html', {"page" : page})