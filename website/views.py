from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))
def aboutMyself(request):
    return HttpResponse("I am Yulia Mikhaylova and I want to learn Django!")