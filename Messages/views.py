from django.http import request
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Quote, Message
# Create your views here.

def index(request):
    if request.method == "POST":
        quote_form = Quote(request.POST)
        if quote_form.is_valid():
            quote_form.save();
            messages.info(request, "We will be in contact")
            return redirect('/')
        else:
            messages.info(request, "Enter valid details")
            return redirect('/')
    else:
        quote_form = Quote()
    return render(request, "index.html", {'quote_form': quote_form})

def contacts(request):
    if request.method == "POST":
        message_form = Message(request.POST)
        if message_form.is_valid():
            message_form.save();
            messages.info(request, "Message received we will stay in contact")
            return redirect("contacts")
        else:
            messages.info(request, "Enter valid information")
            return redirect("contacts")
    else:
        message_form = Message()
    return render(request, "contacts.html", {'message_form': message_form})
