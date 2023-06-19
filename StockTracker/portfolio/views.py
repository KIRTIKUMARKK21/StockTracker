from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required




@login_required
def home(request):
    return render(request,'portfolio.html')


@login_required
def analysis(request):
    return redirect("http://localhost:8501")
    
# Create your views here.
