from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    return HttpResponse('안녕하세요')