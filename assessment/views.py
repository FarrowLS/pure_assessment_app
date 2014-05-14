from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

def index(request):
    indextext = '[some test text: Your tests]'
    context = {'text1': indextext,}  
    return render(request, 'assessment/index.html', context)
    # return HttpResponse("You are at assessment index!")
