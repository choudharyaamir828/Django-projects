from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def students_list(request):
    students = [{
        'name':'John Doe',
        'age':21,
        'course':'Computer Science'
    }]
    return HttpResponse('Students List: ' + str(students))
