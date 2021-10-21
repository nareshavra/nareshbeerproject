from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s='Hello welcome to django classes.mister,django is a nursery concept'
    return HttpResponse(s)
