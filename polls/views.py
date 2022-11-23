from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from django.http import HttpResponse
from .models import Question


def index(request):

    questionLista = Question.objects.all()

