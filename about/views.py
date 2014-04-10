# from django.http import HttpResponse
# from django.template import RequestContext, loader

from django.shortcuts import render


def index(request):
    context = {'text1': 'Hi!!!', 'text2': 'Bye!!!',}
    return render(request, 'about/index.html', context)    
    # return render(request, 'base.html', context)
    # return HttpResponse('Hi!')
