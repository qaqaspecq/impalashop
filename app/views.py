from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from credentials import MpesaAccessToken, LipanaMpesaPpassword

from django.shortcuts import render, redirect
from django.contrib import massages
from .models import Client

# Create your views here.


def index(request):
    data=Client.objects.all()
    context={"data": data}
    return render(request, "index.html", context)


def about(request):
    return render(request, 'index.html')


def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = request.get(api_URL, auth=HTTPBasicAuth(consumer_key,consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]


def pay(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token

        api_url = "https://sandbos.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer%s" % access_token}
        request = {"BusinessShort": LipanaMpesaPpassword.Business_short_code,
                   "Password": LipanaMpesaPpassword.decode_password,
                   "Timestamp": LipanaMpesaPpassword.lipa_time,
                   "TransactionType": "CustomerPayBillOnline",
                   "Amount": amount,
                   "PartyA": phone,
                   "partyB": LipanaMpesaPpassword.Business_short_code,
                   "PhoneNumber": phone,
                   "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                   "AccountReference": "QaqaSoftwares",
                   "TransactionDesc": "Web Development Charges"
                   }
        response = request.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment was a success.Thankyou for shopping with us.")


def stk(request):
    return render(request, 'index.html')



def services(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'index.html')
