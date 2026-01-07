from rest_framework import serializers
from student.models import student
from employees.models import Employee

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ['student_id', 'name', 'branch'] # or '__all__' to include all fields

    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

