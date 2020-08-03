from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from polls.models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        choice = Choice.objects.all()
    except:
        raise Http404("Question doesn't exist f42c7f9c")
    return render(request, 'polls/detail.html', {'question': question, 'choice':choice})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(selected_choice)

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'No choice selected'
        })
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def owner(request):
    return render(request, 'polls/index.html')
