import requests
from django.shortcuts import render, redirect
# from .models import Messages

# Create your views here.
def  index(request):
    return render(request, 'index.html')


def send_sms(request):
    if request.method == "POST":
        data = {
            "contact": request.POST.get('contact'),
            "message": request.POST.get('message'),
        }
        requests.post("http://www.chikka.com:8000/api/send_sms/", data=data)
        return redirect("/")
    return render(request, 'send_sms.html')


def chikka_receiver(request):
    from django.http import HttpResponse
    return HttpResponse({"message": "Success"})


def chikka_proxy(request):
    from django.http import HttpResponse
    return HttpResponse({"message": "Success"})