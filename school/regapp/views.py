from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from .models import Students
def register(request):
    if request.method == "POST":
        user=request.POST['user name']
        lock1=request.POST['password1']
        lock2=request.POST['password2']
        if lock1==lock2:
            if User.objects.filter(username=user).exists():
                messages.info(request,'user name already exists')
                return redirect('regapp:register')

            else:
                member = User.objects.create_user(username=user,password=lock1)
                member.save();
                print("user created")
                return redirect('regapp:login')
        else:
            messages.info(request, 'password are not matching')
            return redirect('regapp:register')

        return redirect('/')
    return render(request,'register.html')


def login(request):
    if request.method =="POST":
        name=request.POST['user name']
        lock = request.POST['password1']
        user=auth.authenticate(username=name,password=lock)
        if user is not None:
            auth.login(request,user)
            return redirect('regapp:formbutton')
        else:
            messages.info(request,'invalid')
            return redirect('regapp:login')

    return render(request,'login.html')

def formbutton(request):
    return render(request,'formbutton.html')

def form(request):
    if request.method =="POST":
        try:
            name = request.POST.get('name', '')
            dob = request.POST.get('dob', '')
            age = request.POST.get('age', '')
            gender = request.POST.get('gender', '')
            phn = request.POST.get('phone', '')
            mail = request.POST.get('email', '')
            adrs = request.POST.get('address', '')
            dep = request.POST.get('department', '')
            crs = request.POST.get('course', '')
            prs = request.POST.get('purpose', '')
            mtrl = request.POST.get('material', '')
            student = Students(name=name, dob=dob, age=age, gender=gender, phone=phn, email=mail, address=adrs,
                               department=dep, course=crs, purpose=prs, material=mtrl)
            student.save()
            messages.info(request, 'your order is placed')
            auth.logout(request)
            return redirect('regapp:form')
        except:
            messages.info(request,'enter your details')
            return redirect('regapp:form')

    return render(request,'form.html')

