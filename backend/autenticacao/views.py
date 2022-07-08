from django.http import HttpResponse
from django.shortcuts import render


def register(request):
    return HttpResponse('Register Page')


def login(request):
    return HttpResponse('Login Page')
