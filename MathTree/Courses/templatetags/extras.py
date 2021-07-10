from django.template import Library
import ast
register = Library()

@register.filter
def parse_text_as_list(s) :
    return ast.literal_eval(s)

@register.filter
def get_identifier(l):
    return l[0]

@register.filter
def get_content(l) :
    return l[1]

