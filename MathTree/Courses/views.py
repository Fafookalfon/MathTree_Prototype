from django.shortcuts import render

def courses(request) : 
    return render(request, 'Courses/courses.html')

def sigmatest(request) :
    return render(request, 'Courses/sigmatest.html')