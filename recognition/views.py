from django.contrib.auth.models import User
from django.shortcuts import render
from requests import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
def home(request):
    return render(request, 'recognition/home.html')

def surat_al_fatiha_reading(request):
    return render(request, 'recognition/surat_al_fatiha_reading.html')

def surat_al_kawthar_reading(request):
    return render(request, 'recognition/surat_al_kawthar_Reading.html')

def surat_al_nas(request):
    return render(request, 'recognition/surat_al_nas.html')
def surat_al_nas_reading(request):
    return render(request,'recognition/surat_al_nas_reading.html')

def welcome(request):
    return render(request, "recognition/welcome.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "كلمات المرور غير متطابقة")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود بالفعل")
        else:
            user = User.objects.create_user(username=username, password=password1)
            user.save()
            messages.success(request, "تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
            return redirect("login")

    return render(request, "recognition/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect("home")  # Redirect to home page after login
        # else:
        #     messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة")

        # request.session['user'] = username  # Store username in session (optional)
        return redirect('home')  # Redirect to home page

    return render(request, "recognition/login.html")

