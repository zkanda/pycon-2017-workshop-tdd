from django.shortcuts import render

# Create your views here.
def  index(request):
    return render(request, 'index.html')


def send_sms(request):
    return render(request, 'send_sms.html')