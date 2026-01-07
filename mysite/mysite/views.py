from urllib import request
from django.http import HttpResponse
from django.shortcuts import render

from employees.models import Employee
def home(request):
    return render(request, "home.html")


def home2(request):
    emp = Employee.objects.all()
    context = {
        "employees": emp
    }

    return render(request, "home2.html", context)