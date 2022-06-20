# write this full****
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import View
from employee.forms import EmployeeForm
from django.contrib import messages
# Create your views here.
#def index(request):
#    return render(request,"home.html")

#def login(request):
#    return render(request,"login.html")

class indexview(View):
    def get(self,request):
        return render(request,"home.html")

class loginview(View):
    def get(self,request):
        return render(request,"login.html")

    def post(self,request):
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return render(request,"login.html")

class registrationview(View):
    def get(self,request):
        return render(request,"registration.html")
    def post(self,request):
        print(request.POST.get("f_name"))
        print(request.POST.get("l_name"))
        print(request.POST.get("u_name"))
        print(request.POST.get("pwd"))
        return render(request,"registration.html")

class EmployeeCreateView(View):
    form_class=EmployeeForm
    template_name="emp-add.html"
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form=self.form_class(request.POST)
        print(request.POST)
        if form.is_valid():
            print("cleaned_data")
            print(form.cleaned_data)
            print(form.cleaned_data.get("emp_id"))
            print(form.cleaned_data.get("emp_name"))
            print(form.cleaned_data.get("designation"))
            print(form.cleaned_data.get("salary"))
            print(form.cleaned_data.get("email"))
            print(form.cleaned_data.get("experience"))
            messages.success(request,"profile added successfully")
            # return render(request,self.template_name,{"form":form})
            return redirect("emp-add")
        else:
            messages.error(request,"profile adding failed")
            # return render(request, self.template_name, {"form": form})
            return render(request,self.template_name,{"form":form})
