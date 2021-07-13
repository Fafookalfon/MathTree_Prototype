from django.template import Library
import ast
from ..models import *
register = Library()

@register.filter
def parse_text_as_list(s) :
    return ast.literal_eval(s)

@register.filter
def get_identifier(l):
    return l[0]

@register.filter
def get_zero_field(l) :
    return l[0]

@register.filter
def get_first_field(l) :
    return l[1]

@register.filter
def get_second_field(l) :
    return l[2]

@register.filter
def get_third_field(l) :
    return l[3]

@register.filter
def get_fourth_field(l) :
    return l[4]

@register.filter
def get_associated_exercise_fields(ex_name) : 
    return [Exercise.objects.filter(name=ex_name).first().questions, Exercise.objects.filter(name=ex_name).first().hints, Exercise.objects.filter(name=ex_name).first().solutions]

@register.filter
def get_last_page(selected_page) :

        last = 1
        for page in ChapterPage.objects.filter(chapter__name=selected_page.chapter.name) :
            if page.index > last : last = page.index
        
        return last