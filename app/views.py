from django.shortcuts import render

from app.models import registr, candidate,admregister
from django.shortcuts import render, redirect, HttpResponse
# from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
# from django.conf import settings
# from django.conf.urls.static import static


# Create your views here.


def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        address = request.POST['address']
        age = request.POST['age']
        mobile = request.POST['mobile']
        dob = request.POST['dob']
        form = registr(username=username, address=address, age=age, mobile=mobile, dob=dob)
        form.save()
        print('saved')
        return HttpResponse('registerd')
    else:
        return render(request, 'registration.html')


def can(request):
    if request.method == 'POST':
        name = request.POST['username']
        location = request.POST['location']
        party = request.POST['party']
        state = request.POST['state']
        form = candidate(name=name, location=location, party=party, state=state)
        form.save()
        print('saved')
        return HttpResponse('registered')
    else:
        return render(request, 'can.html')


def show(request):
    form= registr.objects.all()
    return render(request, 'show.html', {'add1': form})

def candshow(request):
    form= candidate.objects.all()
    return render(request, 'candidateshow.html', {'add1': form})



def admregistr(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        email = request.POST['email']
        form=admregister(name=name,password=password,email=email)
        form.save()
        print('saved')
        return HttpResponse('registerd')
    else:
        return render(request, 'adminreg.html')


def loginn(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        m = []
        n = []
        u = admregister.objects.all()
        print(u)
        for i in u:
            m.append(i.name)
            n.append(i.password)
        if (name in m) & (password in n):
            return redirect('/app/show/')
        else:
            return HttpResponse('Incorrect Entry')
    else:
        return render(request, 'admin.html')


def logout1(request):
    logout(request)
    return redirect("/app/login/")
def home(request):
    return render(request,'home.html')
def h(request):
    return render(request,'index.html')

def finall(request):
    if request.method=="POST":
        c = request.POST.getlist('activate')
        for i in c:
            h = registr.objects.get(id=i)
            h.activate=1
            h.save()
            return HttpResponse('activated')

    else:
        form=registr.objects.all()
        return render(request,'show.html',{'add1':form})
def validation(request):
    if request.method=='POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        print(mobile)
        u = registr.objects.all()
        print(u)
        for i in u:
            if(i.username==name) & (i.mobile==mobile)&(i.activate == 1):
                return redirect('/app/candidateshow/')
            else:
                pass

    else:
        return render(request, 'votervalidation.html')