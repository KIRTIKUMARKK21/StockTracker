from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from .forms import UserRegisterForm
from django.contrib.sites.shortcuts import get_current_site  
from django.template.loader import render_to_string   
from django.utils.encoding import force_bytes, force_str  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.contrib.auth.models import User  
from django.core.mail import EmailMessage  
from .token import account_activation_token  
from django.http import HttpResponse
from django.contrib.auth import get_user_model


def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save();
            username=form.cleaned_data.get('username')
            login(request,user)
            return redirect('portfolio-home')
               
    else:
        form=UserRegisterForm()
    return render(request,'register.html',{'form':form})





def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        print("YES")
        if form.is_valid():
            print("Yes")
            user=form.get_user();
            login(request,user)
            return redirect("portfolio-home")
            
        
    else:
        form=AuthenticationForm();
    return render(request,'login.html',{'form':form})
    
    
    
    
    
    
 
 
    
def logout_view(request):
    logout(request)
    return redirect('home-page')
    
    






























# def register(request):
#     if request.method=='POST':
#         form=UserRegisterForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             # user.is_active=False
#             user.save();
#             current_site=get_current_site(request)
#             mail_subject='Activation Link has been sent to your email id'
#             message=render_to_string('acc_active_email.html',
#                                      {
#                                          'user':user,
#                                          'domain':current_site.domain,
#                                          'uid':urlsafe_base64_encode(force_bytes(user.pk)),
#                                          'token':account_activation_token.make_token(user),   
                                         
#                                      }
#             )
#             to_email = form.cleaned_data.get('email')  
#             email = EmailMessage(  
#                         mail_subject, message, to=[to_email]  
#             )  
#             email.send()  
#             return HttpResponse('Please confirm your email address to complete the registration')  
#     else:
#         form=UserRegisterForm();
#     return render(request,'register.html',{'form':form})


def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('portfolio-home')
    else:  
        return HttpResponse('Activation link is invalid!')  
    
    
    
    
    
    
    
    
