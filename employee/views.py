# # write this full****
# from django.shortcuts import render,redirect
#from django.http import HttpResponse
# from django.views.generic import View
# from employee.forms import EmployeeForm
# from django.contrib import messages
# # Create your views here.
# #def index(request):
# #    return render(request,"home.html")
#
# #def login(request):
# #    return render(request,"login.html")
#
# class indexview(View):
#     def get(self,request):
#         return render(request,"home.html")
#
# class loginview(View):
#     def get(self,request):
#         return render(request,"login.html")
#
#     def post(self,request):
#         print(request.POST.get("u_name"))
#         print(request.POST.get("pwd"))
#         return render(request,"login.html")
#
# class registrationview(View):
#     def get(self,request):
#         return render(request,"registration.html")
#     def post(self,request):
#         print(request.POST.get("f_name"))
#         print(request.POST.get("l_name"))
#         print(request.POST.get("u_name"))
#         print(request.POST.get("pwd"))
#         return render(request,"registration.html")
#
# class EmployeeCreateView(View):
#     form_class=EmployeeForm
#     template_name="emp-add.html"
#     def get(self,request):
#         form=self.form_class()
#         return render(request,self.template_name,{"form":form})
#     def post(self,request):
#         form=self.form_class(request.POST)
#         print(request.POST)
#         if form.is_valid():
#             print("cleaned_data")
#             print(form.cleaned_data)
#             print(form.cleaned_data.get("emp_id"))
#             print(form.cleaned_data.get("emp_name"))
#             print(form.cleaned_data.get("designation"))
#             print(form.cleaned_data.get("salary"))
#             print(form.cleaned_data.get("email"))
#             print(form.cleaned_data.get("experience"))
#             messages.success(request,"profile added successfully")
#             # return render(request,self.template_name,{"form":form})
#             return redirect("emp-add")
#         else:
#             messages.error(request,"profile adding failed")
#             # return render(request, self.template_name, {"form": form})
#             return render(request,self.template_name,{"form":form})

from django.shortcuts import render,redirect
from employee.models import Employee
from django.contrib import messages
from django.views import View
from employee.forms import EmployeeCreateForm,UserRegistrationForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator


#decoretor for authenticate

def signin_requied(fn):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,*kwargs)
        else:
            messages.error(request,"you must login")
            return redirect("signin")
    return wrapper


@method_decorator(signin_requied,name="dispatch")
class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form=EmployeeCreateForm()
        return render(request,"add-emp.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=EmployeeCreateForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # Employee.objects.create(
            #     emp_id=form.cleaned_data.get("emp_id"),
            #     emp_name=form.cleaned_data.get("emp_name"),
            #     designation=form.cleaned_data.get("designation"),
            #     salary=form.cleaned_data.get("salary"),
            #     email=form.cleaned_data.get("email"),
            #     experience=form.cleaned_data.get("experience"),
            # )
            messages.success(request, "profile added successfully")
#           return render(request,"emp-add.html",{"form":form})
            return redirect("emp-list")

        else:
            messages.error(request,"profile not added")
            return render(request,"add-emp.html",{"form":form})

@method_decorator(signin_requied,name="dispatch")
class EmployeeListView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.all()  #takeing all employee details (qs is a object )
        return render(request,"emp-list.html",{"employees":qs})



class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):
        qs=Employee.objects.get(emp_id=kwargs.get("emp_id"))
        return render(request,"emp-detail.html",{"employee":qs})



class EmployeeEditView(View):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("e_id")
        employee=Employee.objects.get(emp_id=eid)
        form=EmployeeCreateForm(instance=employee)
        return render(request,"emp-edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        eid = kwargs.get("e_id")
        employee = Employee.objects.get(emp_id=eid)
        form = EmployeeCreateForm(request.POST,instance=employee,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "profile updated successfully")
            return redirect("emp-add")

        else:
            messages.error(request, "profile not updated")
            return render(request, "emp-add.html", {"form": form})


@signin_requied
def remove_employee(request,*args,**kwargs):
    eid = kwargs.get("e_id")
    employee = Employee.objects.get(emp_id=eid)
    employee.delete()
    messages.success(request,"profile updated successfully")
    return redirect("emp-list")


@signin_requied
def index(request,*args,**kwargs):
    return render(request,"base.html")


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account created successfully")
            return redirect("signin")
        else:
            messages.error(request,"Error in creation")
            return render(request,"register.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("success")
                return redirect("index")
            else:
                messages.error(request,"invalid credential")
                return render(request,"login.html",{"form":form})

def sign_out(request,*args,**kwargs):
    logout(request)
    return redirect("signin")















