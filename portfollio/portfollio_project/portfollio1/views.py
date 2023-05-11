from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, request

def Myportfollio (request):

    return render(request, 'mycv.html')