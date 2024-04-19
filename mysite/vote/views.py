from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.db.models import F

from .models import Question, Vote

# Create your views here.

def index(request):
    data = Question.objects.all()
    return render(request, "vote/index.html", {"q_list": data})


def question(request, _id):
    data = get_object_or_404(Question, pk=_id)
    return render(request, "vote/question.html", {"q": data})


def result(request, _id):
    data = get_object_or_404(Question, pk=_id)
    return render(request, "vote/results.html", {"q": data})


def vote(request, _id):
    data = get_object_or_404(Question, pk=_id)
    choice = get_object_or_404(Vote, pk=request.POST["vote"])
    choice.count = F("count") + 1
    choice.save()
    return HttpResponseRedirect(reverse("vote:result", args=(data.id, )))
