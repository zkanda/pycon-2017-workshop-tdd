import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Messages

# Create your views here.
def  index(request):
    return render(request, 'index.html', {"messages": Messages.objects.all()})


def send_sms(request):
    if request.method == "POST":
        data = {
            "contact": request.POST.get('contact'),
            "message": request.POST.get('message'),
        }
        requests.post("http://www.chikka.com:8000/api/send_sms/", data=data)
        return redirect("/")
    return render(request, 'send_sms.html')


@csrf_exempt
def chikka_receiver(request):
    Messages.objects.create(
        mobile_number=request.POST.get('mobile_number'),
        message=request.POST.get('message')
    )
    return HttpResponse({"message": "Success"})


def chikka_proxy(request):
    return HttpResponse({"message": "Success"})