#coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	#return HttpResponse('Hello World!')
    
    #return render(request, 'index.html')
    
    #texts = ['Lorem ipsum', 'dolor sit amet', 'consectetur']
    #context = {
    #    'title': 'django e-commerce',
    #    'texts': texts
    #}
    #return render(request, 'index.html', context)

    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


