from django.contrib import admin

# Register your models here.

from .models import *

# INLINES

class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1

class ChapterPageInline(admin.StackedInline):
    model = ChapterPage
    extra = 1

# ADMINS

class CourseAdmin(admin.ModelAdmin):
    inlines = [ChapterInline]

class ChapterAdmin(admin.ModelAdmin):
    inlines = [ChapterPageInline]
    search_fields = ['course__name']

class ChapterPageAdmin(admin.ModelAdmin):
    search_fields = ['chapter__name']

from .models import *

admin.site.register(Course, CourseAdmin)
admin.site.register(CourseTree)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(ChapterPage, ChapterPageAdmin)
admin.site.register(Exercise)
