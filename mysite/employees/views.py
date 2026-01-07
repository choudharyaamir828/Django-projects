from django.shortcuts import render, get_object_or_404
from .models import Employee
from django.http import HttpResponse

# Create your views here.

def employee_detail(request, pk):

        employee = get_object_or_404(Employee, pk=pk)
        context = {
            'employee': employee,  
        }

        return render(request, 'employees_details.html', context)