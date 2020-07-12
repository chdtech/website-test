from django.http import JsonResponse
from django.shortcuts import render

def json(request):
    responseData = {
        'name' : 'Ava',
        'age' : 21
    }

    return JsonResponse(responseData)

def index(request):
    return render(request,'index.html')