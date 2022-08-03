# from django import forms
#
# class EmployeeForm(forms.Form):
#     emp_id=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter id"}))
#     emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter name"}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"enter designation"}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"enter salary"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"enter experience"}))
#     def clean(self):
#         cleaned_data=super().clean()
#         exp=cleaned_data.get("experience")
#         if exp<0:
#             msg="invalid exp"
#             self.add_error("experience",msg)

# from django import forms
# class EmployeeCreateForm(forms.Form):
#     emp_id=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     emp_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))
#     email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
#     experience=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control"}))

from django import forms
from employee.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets={
            "emp_id":forms.TextInput(attrs={"class":"form-control"}),
            "emp_name":forms.TextInput(attrs={"class":"form-control"}),
            "designation":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "experience":forms.NumberInput(attrs={"class":"form-control"})
        }

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password1","password2" ]

class LoginForm(forms.Form):
    username=forms.CharField(label="username")
    password=forms.CharField(label="password")



