from django.shortcuts import render
from django.views.generic import View
from calculator.forms import OperationForm

# #Create your views here.
class HomeView(View):
    def get(self,request):
        return render(request,"calc-home.html")

class AddView(View):
    def get(self,request):
        form=OperationForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)+int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=int(n1)+int(n2)
            print(form.cleaned_data)
            return render(request,"add.html",{"res":result,"form":form})
        else:
            return render(request,"add.html",{"form":form})
class SubView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"sub.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)-int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=n1-n2
            return render(request,"sub.html",{"res":result,"form":form})
        else:
            return render(request,"sub.html", {"form": form})

class MultiplicationView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"multiplication.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)*int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=int(n1)*int(n2)
            return render(request,"multiplication.html",{"res":result,"form":form})
        else:
            return render(request,"multiplication.html",{"form":form})



class DivitionView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"divition.html",{"form":form})
    def post(self,request):
        # n1=request.POST.get("num1")
        # n2=request.POST.get("num2")
        # result=int(n1)/int(n2)
        # print(result)
        form=OperationForm(request.POST)
        if form.is_valid():
            n1=form.cleaned_data.get("num1")
            n2=form.cleaned_data.get("num2")
            result=int(n1)/int(n2)
            return render(request,"divition.html",{"res":result,"form":form})
        else:
            return render(request,"divition.html", {"form": form})

class WordcountView(View):
    def get(self,request):
        return render(request,"wordcount.html",)
    def post(self,request):
        word=request.POST.get("word")
        words=word.split(" ")
        wc={}
        for w in words:
            if w not in wc:
                 wc[w]=1
            else:
                 wc[w]+=1
        print(wc)
        return render(request,"wordcount.html",{"res":wc})

class PrimeView(View):
    def get(self,request):
        form = OperationForm()
        return render(request,"prime.html",{"form":form})
    def post(self,request):
        n1=int(request.POST.get("num1"))
        n2=int(request.POST.get("num2"))
        prime=[]
        for i in range(n1,n2+1):
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                prime.append(i)
        print(prime)
        return render(request,"prime.html",{"result":prime})