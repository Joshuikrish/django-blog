from django.contrib import admin
from .models import Question, Choice, Blog
from django.utils.html import mark_safe
# Register your models here.

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'votes', 'question')

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'thumbnail')
    def thumbnail(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"

    thumbnail.short_description = 'Thumbnail'

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Blog, BlogAdmin)