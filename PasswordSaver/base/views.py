from asyncio.windows_events import NULL
from contextlib import redirect_stderr
from http.client import HTTPConnection, HTTPResponse
from urllib import request, response
from wsgiref.util import request_uri
from django.shortcuts import render
from base.models import User, WebAppPassword, CardPassword
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from encrypt_util import *
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

            if check_password(password, user.password):
                request.session['user_id'] = user.user_id
                return redirect('/home')
            else:
                messages.error(request, 'Username or Password is incorrect')

        except:
            messages.error(request, 'User does not exist')

        # user_auth = authenticate(request,username=username,password=password)

    return render(request, 'login.html')


def register(request):
    if request.POST.get('email') and request.POST.get('password'):
        data = User()
        data.username = request.POST.get('email')
        data.password = make_password(request.POST.get('password'))
        data.save()
        user = User.objects.get(username=request.POST.get('email'))
        request.session['user_id'] = user.user_id
        return render(request, 'home.html', {'user': user})

    return render(request, 'register.html')


def about(request):
    print(request.session['user_id'])
    return render(request, 'about.html')


def home(request):
    return render(request, 'home.html')


def website(request):
    data = WebAppPassword.objects.filter(user_id=request.session['user_id'])
    return render(request, 'website_password.html', {'website': data})


def card(request):
    data = CardPassword.objects.filter(user_id=request.session['user_id'])
    return render(request, 'card_password.html', {'card': data})


def add_web_pass(request):

    user_id = request.session['user_id']
    if request.method == 'POST':
        data = WebAppPassword()
        data.username = request.POST.get('username')
        data.password = encrypt(request.POST.get('password'))
        data.title = request.POST.get('title')
        data.web_address = request.POST.get('Website_Address')
        data.user_id = user_id
        if request.POST.get('note'):
            data.note = request.POST.get('note')
        data.save()
        return redirect('/website')
    return render(request, 'addpassword_website.html', {'user': request.session['user_id']})


def add_card_pass(request):

    user_id = request.session['user_id']
    if request.method == 'POST':
        data = CardPassword()
        data.card_holder_name = request.POST.get('name')
        data.card_number = request.POST.get('number')
        data.card_exp = request.POST.get('exp_mm_yy')
        data.card_cvv = encrypt(request.POST.get('cvv'))
        data.user_id = user_id
        data.card_atm_pin = encrypt(request.POST.get('pin'))
        data.save()
        return redirect('/card')
    return render(request, 'addpassword_card.html', {'user': request.session['user_id']})


def website_details(request, pk):
    data = WebAppPassword.objects.get(webapp_id=pk)
    data.password = decrypt(data.password)
    return render(request, 'website_details.html', {'details': data})


def card_details(request, pk):
    data = CardPassword.objects.get(card_id=pk)
    data.card_cvv = decrypt(data.card_cvv)
    data.card_atm_pin = decrypt(data.card_atm_pin)
    return render(request, 'card_details.html', {'details': data})


def website_delete(request,pk):
    data = WebAppPassword.objects.get(webapp_id=pk)
    data.delete()
    return redirect('/website')


def card_delete(request,pk):
    data = CardPassword.objects.get(card_id=pk)
    data.delete()
    return redirect('/card')


# def generateKey(string, key): 
#     key = list(key) 
#     if len(string) == len(key): 
#         return(key) 
#     else: 
#         for i in range(len(string) -len(key)): 
#             key.append(key[i % len(key)]) 
#     return("" . join(key)) 
  
# def encryption(string, key): 
#     encrypt_text = [] 
#     for i in range(len(string)): 
#         x = (ord(string[i]) +ord(key[i])) % 26
#         x += ord('A') 
#         encrypt_text.append(chr(x)) 
#     return("" . join(encrypt_text)) 

# def decryption(encrypt_text, key): 
#     orig_text = [] 
#     for i in range(len(encrypt_text)): 
#         x = (ord(encrypt_text[i]) -ord(key[i]) + 26) % 26
#         x += ord('A') 
#         orig_text.append(chr(x)) 
#     return("" . join(orig_text)) 

