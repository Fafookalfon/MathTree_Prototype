from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Course

class courses(ListView) : 

    template = 'Courses/courses.html'
    context_object_name = 'Courses_list'

    def get_queryset(self) : 
        return Course.objects.all()

'''
def courses(request) : 
    return render(request, 'Courses/courses.html')
'''