from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is homepage of secondproject" )

def about(request):
    return HttpResponse("This is about page of secondproject" ) 
