from django.db import models
from django.contrib import admin

big_number = 100000000

# Create your models here.

class Course(models.Model) :
    name = models.CharField(max_length = big_number)

    def __str__(self) :
        return self.name

    x_position = models.IntegerField(default=0)
    y_position = models.IntegerField(default=0)

class Prerequisite(models.Model) :

    prerequisite = models.ForeignKey(Course, related_name = "prerequisite", on_delete=models.CASCADE)
    target = models.ForeignKey(Course, related_name = "target", on_delete=models.CASCADE)
    comment = models.TextField()

    
class CourseTree(models.Model) : 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    data = models.CharField(max_length = big_number)


class Chapter(models.Model) : 
    index = models.IntegerField(default = -1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length = big_number)
    prerequisites = models.CharField(max_length = big_number)

    '''
    @admin.display(
        boolean=True,
        ordering='index'
    )
    '''

    def __str__(self) :
        return (f"{self.course}, Chapter {self.index}, {self.name}")

class Exercise(models.Model) : 
    
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    name = models.CharField(default = "name", max_length=big_number)
    difficulty = models.IntegerField(default = 1)
    questions = models.CharField(max_length = big_number)
    hints = models.CharField(max_length = big_number)
    solutions = models.CharField(max_length = big_number)

    def __str__(self) :
        return self.name

class ChapterPage(models.Model) : 
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    index = models.IntegerField()
    content = models.CharField(max_length = big_number)

    def __str__(self) :
        return (self.chapter.__str__() + ', Page ' + str(self.index))





