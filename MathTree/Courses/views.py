from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from .models import Course, Chapter, ChapterPage, Prerequisite, Comment
import json
from random import randint

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

def page_comment_view(request, course_name, chapter_index, page_index ) :

    page = ChapterPage.objects.filter(chapter__course__name=course_name, chapter__index=chapter_index, index=page_index).first()
    captcha = enigma()
    return render(request, 'Courses/page_comment.html', {"page" : page, "grand_nombre_lettres" : captcha.get("grand_nombre_lettres"), "petit_nombre_lettres" :  captcha.get("petit_nombre_lettres"), "operation" :  captcha.get("operation"), "solution" :  captcha.get("solution")})

def send_comment(request, course_name, chapter_index, page_index, solution) :

    course = Course.objects.filter(name=course_name).first()
    chapter = course.chapter_set.filter(index=chapter_index).first()
    page = chapter.chapterpage_set.filter(index=page_index).first()

    if not request.method == 'POST' :
        return render(request, "Courses/comment_feedback.html", {"page" : page, "comment_feedback" : "Quelque chose n'a pas marché..."})
    
    if str(request.POST.get("solution")) != str(solution) :
        return render(request, "Courses/comment_feedback.html", {"page" : page, "comment_feedback" : "Quelque chose n'a pas marché..."})
    
    new_comment = Comment(course=course, chapter=chapter, page= page, title=request.POST.get("title"), content=request.POST.get("content"))
    new_comment.save()
    return render(request, "Courses/comment_feedback.html", {"page" : page, "comment_feedback" : "Merci pour votre commentaire !"}) 

### This is dedicated to generating all the json necessary for the tree rendering. ###

def prerequisite_to_json(Prerequisite) :

    result = {}
    result.update({"id" : f"{Prerequisite.prerequisite.name} to {Prerequisite.target.name}" })
    result.update({"source" : Prerequisite.prerequisite.name})
    result.update({"target" : Prerequisite.target.name})
    result.update({"size" : 3})
    result.update({"hover_color" : "#0000FF"})

    return result

def course_to_json(course) : 

    result = {}
    result.update({"id" : course.name})
    result.update({"label" : course.name})
    result.update({"x" : course.x_position})
    result.update({"y" : course.y_position})
    result.update({"size" : 6})

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

### Those functions are pure utilities. ###

def enigma() :

    operations = ["plus", "moins"]
    nombres = ['zéro', 'un', 'deux', 'trois', 'quatre', 'cinq', 'six', 'sept', 'huit', 'neuf', 'dix', 'onze', 'douze', 'treize', 'quatorze', 'quinze', 'seize', 'dix-sept', 'dix-huit', 'dix-neuf', 'vingt', 'vingt et un', 'vingt-deux', 'vingt-trois', 'vingt-quatre', 'vingt-cinq', 'vingt-six', 'vingt-sept', 'vingt-huit', 'vingt-neuf', 'trente', 'trente et un', 'trente-deux', 'trente-trois', 'trente-quatre', 'trente-cinq', 'trente-six', 'trente-sept', 'trente-huit', 'trente-neuf', 'quarante', 'quarante et un', 'quarante-deux', 'quarante-trois', 'quarante-quatre', 'quarante-cinq', 'quarante-six', 'quarante-sept', 'quarante-huit', 'quarante-neuf', 'cinquante', 'cinquante et un', 'cinquante-deux', 'cinquante-trois', 'cinquante-quatre', 'cinquante-cinq', 'cinquante-six', 'cinquante-sept', 'cinquante-huit', 'cinquante-neuf', 'soixante', 'soixante et un', 'soixante-deux', 'soixante-trois', 'soixante-quatre', 'soixante-cinq', 'soixante-six', 'soixante-sept', 'soixante-huit', 'soixante-neuf', 'soixante-dix', 'soixante et onze', 'soixante-douze', 'soixante-treize', 'soixante-quatorze', 'soixante-quinze', 'soixante-seize', 'soixante-dix-sept', 'soixante-dix-huit', 'soixante-dix-neuf', 'quatre-vingts', 'quatre-vingt-un', 'quatre-vingt-deux', 'quatre-vingt-trois', 'quatre-vingt-quatre', 'quatre-vingt-cinq', 'quatre-vingt-six', 'quatre-vingt-sept', 'quatre-vingt-huit', 'quatre-vingt-neuf', 'quatre-vingt-dix', 'quatre-vingt-onze', 'quatre-vingt-douze', 'quatre-vingt-treize', 'quatre-vingt-quatorze', 'quatre-vingt-quinze', 'quatre-vingt-seize', 'quatre-vingt-dix-sept', 'quatre-vingt-dix-huit', 'quatre-vingt-dix-neuf', 'cent']
    
    grand_nombre_int = randint(40,60)
    petit_nombre_int = randint(0,20)
    grand_nombre_lettres = nombres[grand_nombre_int]
    petit_nombre_lettres = nombres[petit_nombre_int]
    operation = operations[randint(0,1)]
    solution = grand_nombre_int

    if operation == "plus" :
        solution += petit_nombre_int
    
    else : solution -= petit_nombre_int

    return {"grand_nombre_lettres" : grand_nombre_lettres, "petit_nombre_lettres" : petit_nombre_lettres, "operation" : operation, "solution" : str(solution)}
