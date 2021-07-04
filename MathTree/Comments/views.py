from django.shortcuts import render

def SendComment(request) :
    return render(request, 'Comments/comments.html')