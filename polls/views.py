from django.http import HttpResponse
from django.http import Http404
from polls.models import Question
from django.template import loader
from django.shortcuts import render
from django.db import models

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist f42c7f9c")
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse(f'you are at {question_id}')




def results(request, question_id):
    response = "You're looking at the results f42c7f9c  of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on  f42c7f9c question %s." % question_id)

def owner(request):
    return render(request, 'polls/index.html')