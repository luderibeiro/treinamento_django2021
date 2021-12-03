from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
class QuestionAdmin(admin.ModelAdmin):
    inlines = (ChoiceInline,)
    list_display = ('question_text', 'pub_date',)

admin.site.register(Question, QuestionAdmin)
