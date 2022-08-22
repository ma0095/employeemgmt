from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_id=models.CharField(max_length=80,primary_key=True)
    profile_pic=models.ImageField(upload_to="profilepic",null=True)
    emp_name=models.CharField(max_length=80)
    designation=models.CharField(max_length=80)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    experience=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.emp_name
