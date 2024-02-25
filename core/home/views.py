from django.shortcuts import redirect, render

from django.http import HttpResponse
from vege.seed import *
from .utils import send_email_to_client, send_email_with_attachment

from django.conf import settings 

def send_email(request):
  subject = "This email is from Django server with Attachment"
  message = "Hey Please, find this attachment file with this Email"
  recipient_list = ["rahulverma9449@gmail.com"]
  file_path = f"{settings.BASE_DIR}/main/xlsx"
  
  send_email_with_attachment(subject , message , recipient_list, file_path)
  send_email_to_client()
  return redirect('/')


def home(request):
  seed_db(100)

  peoples = [
    {'name': 'Abhijeet verma', 'age': 26},
    {'name': 'rahul verma', 'age': 32},
    {'name': 'ankit verma', 'age': 17},
    {'name': 'pawan verma', 'age': 24},
    {'name': 'sandeep verma', 'age': 16},
    {'name': 'raja verma', 'age': 21},
  ]

  vegetables = ['Pumpkin', 'tomato', 'potato']
  

  return render(request, "home/index1.html", context= {'page': 'Django 2024 Tutorial', 'peoples':peoples,'vegetables':vegetables})

def about(request):
  contact = {'page' : 'about'}
  return render(request,"home/about.html", contact)


def contact(request):
  contact = {'page' : 'Contact'}
  return render(request,"home/contact.html", contact)

def success_page(request):
  print("*" * 10)
  contact = {'page' : 'Contact'}
  return HttpResponse("<h2>Hey, This is success_page.</h2>")

