from django.shortcuts import render
from myapp.form import StuForm

def index(request):
    stu= EmpForm()
    return render(request,"index.html",{'form':stu})