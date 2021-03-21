from django.shortcuts import render
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login
from django.shortcuts import get_object_or_404
from django.db.models import Max
from django.http import JsonResponse
from django.urls import reverse
from .models import Patient, Doctor, History
import datetime

# Create your views here.


def index(request):

    # if request.user.is_authenticated:
    # 	return redirect('personalInfo')
    # notices = Notice.objects.all()
    # parameters = {'notices' : notices}
    if request.method == 'POST':
        # print('request is post')
        username = request.POST['email']
        password = request.POST['password2']
        print(username)
        print(password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # print('user is not None')
            login(request, user)
            return redirect('personalInfo')
        else:
            param = {'error_message': 'Invalid Credentials'}
            return render(request, 'mainsite/index.html', param)
    return render(request, 'mainsite/index.html')
    # return HttpResponse('Hello')


def personalInfo(request):
    if(Patient.objects.filter(user=request.user)):
        
        return render(request, 'mainsite/phome.html')
    else:
        return render(request, 'mainsite/dhome.html')


def counsel(request):
    if request.method == 'POST':
        # print('request is post')patientid, complication, prescription
        date = datetime.datetime.now()
        patientid = request.POST['patientid']
        complication = request.POST['complication']
        prescription = request.POST['prescription']
        doctor = request.user.username
        history = History(date=date, complication=complication,
                          patient=patientid, doctor=doctor, prescription=prescription)
        history.save()
        # print(username)
        # print(password)
        # user = authenticate(request, username=username, password=password)
        # if user is not None:
        #     # print('user is not None')
        #     login(request, user)
        #     return redirect('personalInfo')
        # else:
        #     param = {'error_message': 'Invalid Credentials'}
        #     return render(request, 'mainsite/index.html', param)

    return render(request, "mainsite/dcounsel.html")


def dpatient(request):
    if(Patient.objects.filter(user=request.user)):
        print("hello")
        p = Patient.objects.filter(user=request.user)
        h = History.objects.filter(patient = p[0].user.userid)
        print(h)

        params = {'history' : h}
    #     return render(request, 'mainsite/phome.html', params)
    # else:
    #     return render(request, 'mainsite/dhome.html')


def ddoctor(request):
    if(Patient.objects.filter(user=request.user)):
        return render(request, 'mainsite/phome.html')
    else:
        return render(request, 'mainsite/dhome.html')
