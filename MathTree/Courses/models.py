from django.db import models
from django.contrib import admin

big_number = 100000000

# Create your models here.

class Course(models.Model) :
    name = models.CharField(max_length = big_number)

    def __str__(self) :
        return self.name

    x_position = models.FloatField(default=0)
    y_position = models.FloatField(default=0)
    description = models.TextField(default = "")

class Prerequisite(models.Model) :

    prerequisite = models.ForeignKey(Course, related_name = "prerequisite", on_delete=models.CASCADE)
    target = models.ForeignKey(Course, related_name = "target", on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self) :
        return f"{self.prerequisite.name} to {self.target.name}" 

    
class CourseTree(models.Model) : 

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    data = models.TextField(default = "")


class Chapter(models.Model) : 

    index = models.IntegerField(default = -1)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length = big_number)
    description = models.TextField(default = "")

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
    questions = models.TextField(default = "")
    hints = models.TextField(default = "")
    solutions = models.TextField(default = "")

    def __str__(self) :
        return self.name

class ChapterPage(models.Model) : 
    
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    index = models.IntegerField()
    content = models.TextField(default = "")

    def __str__(self) :
        return (self.chapter.__str__() + ', Page ' + str(self.index))
    
    def is_last_page(self) :
        
        
        for page in ChapterPage.objects.filter(chapter__name=self.chapter.name) :
            if page.index > self.index :
                return False
        
        return True
    
    def is_first_page(self) :

        for page in ChapterPage.objects.filter(chapter__name=self.chapter.name) :
            if page.index < self.index :
                return False
        
        return True

    
    def next_index(self) : 
        return self.index + 1

    def previous_index(self) : 
        return self.index - 1 

class Comment(models.Model) : 
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    page = models.ForeignKey(ChapterPage, on_delete=models.CASCADE)
    
    title = models.CharField(default="", max_length=200)
    content = models.TextField(default = "")

    def __str__(self) :
        return self.title



