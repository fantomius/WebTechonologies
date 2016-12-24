from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def new(request):
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    limit = 10

    questions = Question.objects.new()
    paginator = Paginator(questions, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    return render(request, "posts/index.html", {
        'page': page
    })

def popular(request):
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    limit = 10

    questions = Question.objects.popular()
    paginator = Paginator(questions, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page = paginator.page(paginator.num_pages)

    return render(request, "posts/index.html", {
        'page': page
    })

def question(request, id):
    try:
        questionId = int(id)
    except:
        raise Http404

    try:
        question = Question.objects.get(pk=questionId)
    except:
        raise Http404

    answers = Answer.objects.filter(question=question)

    return render(request, "questions/index.html", {
        'question': question,
        'answers': answers
    })

