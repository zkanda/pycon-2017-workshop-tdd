"""sms_survey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from engagement.views import index, send_sms, chikka_proxy, chikka_receiver

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^send_sms/$', send_sms, name='send_sms'),
    url(r'^chikka_receiver/$', chikka_receiver, name='chikka_receiver'),
    

    # This is only need for testing locally
    url(r'^api/send_sms/$', chikka_proxy, name='chikka_proxy')
]
