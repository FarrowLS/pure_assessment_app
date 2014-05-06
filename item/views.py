from django.http import HttpResponse

def index(request):
    return HttpResponse("You're here on the items index page!") 
