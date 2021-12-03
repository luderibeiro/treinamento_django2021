from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, "polls/index.html", {'latest_question_list': latest_question_list, 'titulo': 'Lista de Questões',})