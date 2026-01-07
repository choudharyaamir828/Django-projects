from django.db import models

# Create your models here.


class student(models.Model):
    student_id = models.CharField(max_length = 20)
    name = models.CharField(max_length=30)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name