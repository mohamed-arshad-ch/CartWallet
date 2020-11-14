from django.shortcuts import render

# Create your views here.

#Load landing Page

def index(request):
    try:
        return render(request,'index.html')
    except Exception as e:
        print(e)

#Load register Page

def register(request):
    try:
        return render(request,'register.html')
    except Exception as e:
        print(e)