from django.shortcuts import render
import json

from .models import testing

# Create your views here.

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):
     return render(request, 'home/home.html') 

def index(request):    
    # If you have passed any data through the 'data' property 
    #you can get it here, according to the method used.
    ##if is_ajax(request=request):
        id = request.GET.get('id')
        msg = testing.objects.exclude(id = id).first()
    # Note that we are passing the 'ajax_comments.html' template.
        #return render(request, 'practice.html', {'text': msg, 'id':id})
    ##else:
        ##msg = testing.objects.last()
        return render(request, 'practice.html', {'text': msg, 'id': id} )       

    #comments = Comment.objects.all.first()
    #return render(request, 'practice.html', {'comments': comments})

    