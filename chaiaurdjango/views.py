from django.http import HttpResponse
from django.shortcuts import render
def Home(request):
    # return HttpResponse('Hello World  Iam inside Django')
    return render(request, 'layout.html')
def About(request):
    return HttpResponse('Hello World Iam inside about django ')
def Contact(request):
    return HttpResponse('HEllo world iam inside contact django')
