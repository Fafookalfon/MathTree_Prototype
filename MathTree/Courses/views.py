from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Course, Chapter, ChapterPage, Prerequisite
import json

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

def exercises_view(request, course_name) :

    course = Course.objects.filter(name=course_name).first()
    return render(request, 'Courses/exercises_view.html', {"course" : course})

### This is dedicated to generating all the json necessary for the tree rendering. ###

def prerequisite_to_json(Prerequisite) :

    result = {}
    result.update({"id" : f"{Prerequisite.prerequisite.name} to {Prerequisite.target.name}" })
    result.update({"source" : Prerequisite.prerequisite.name})
    result.update({"target" : Prerequisite.target.name})

    return result

def course_to_json(course) : 

    result = {}
    result.update({"id" : course.name})
    result.update({"label" : course.name})
    result.update({"x" : course.x_position})
    result.update({"y" : course.y_position})
    result.update({"size" : 3})

    return result

def generate_tree_data_as_json() :

    result = { "nodes" : [], "edges" : []  }
    
    for course in Course.objects.all() :
        result["nodes"].append(course_to_json(course))
    
    for prerequisite in Prerequisite.objects.all() :
        result["edges"].append(prerequisite_to_json(prerequisite))
    
    return json.dumps(result)

def general_tree_view(request) : 
    return render(request, "Courses/tree_view.html", context = {"data" : generate_tree_data_as_json()})

