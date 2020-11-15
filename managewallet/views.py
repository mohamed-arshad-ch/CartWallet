from django.shortcuts import render, redirect, HttpResponse
import random
import string
from .models import *
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

# Load landing Page


def index(request):
    try:
        if request.user.is_authenticated:
            return redirect('dash')

        elif request.method == 'GET':
            return render(request, 'index.html')
        else:
            username = request.POST['username']
            password = request.POST['password']

            customuser = CustomeUser.objects.get(
                username=username, password=password)
            if customuser is not None:

                auth.login(request, customuser)

                messages.info(request, 'Login Successfully')
                return redirect('dash')

            else:

                messages.info(request, 'UserName And password Is Error')
                return redirect('index')

    except Exception as e:
        print(e)
        messages.info(request, 'UserName And password Is Error')
        return redirect('index')

# Load register Page


def register(request):
    try:
        if request.method == 'GET':
            return render(request, 'register.html')
        else:
            firstname = request.POST.get('fullname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            mobile = request.POST.get('mobile')
            password = request.POST.get('password')
            reff_code = request.POST.get('reffcode')

            print(reff_code)

            letter = string.ascii_letters
            result = ''.join(random.choice(letter) for i in range(8))
            if reff_code == "":

                customeuser, created = CustomeUser.objects.get_or_create(
                    first_name=firstname, username=username, email=email, mobile_no=mobile, password=password, reff_code=result, refferd_user="")
                messages.info(request, 'Registration Successfully')

                return redirect('index')
            else:
                cust = CustomeUser.objects.get(reff_code=reff_code)

                customeuser, created = CustomeUser.objects.get_or_create(
                    first_name=firstname, username=username, email=email, mobile_no=mobile, password=password, reff_code=result, refferd_user=cust.username)
                messages.info(request, 'Registration Successfully')

                return redirect('index')

    except Exception as e:
        print(e)

# This Logout User
def logout(request):
    auth.logout(request)
    return redirect('index')

# lOad Dash Page
@login_required(login_url='index')
def dash(request):
    try:
        cust = CustomeUser.objects.filter(
            refferd_user=request.user.username).count()
        reward = 0
        reward = cust * 100
        print(cust)
        products = Product.objects.filter(user=request.user)
        cart = Cart.objects.filter(user=request.user)
        totalamount = 0
        for i in cart:
            totalamount = totalamount + i.amount
        return render(request, 'dash.html', {'reward': reward, 'products': products, 'total': totalamount})
    except Exception as e:
        print(e)

#Add Product From Model
@login_required(login_url='index')
def addproduct(request):
    try:
        product_name = request.POST.get('productname')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        Product.objects.create(product_name=product_name,
                               price=price, image=image, user=request.user)
        return redirect('dash')

    except Exception as e:
        print(e)

#View Url For Each Product
@login_required(login_url='index')
def viewproduct(request, id, ref):
    try:
        if request.method == 'GET':
            usr = CustomeUser.objects.get(reff_code=ref)
            product = Product.objects.get(user=usr, id=id)
            return render(request, 'viewproduct.html', {'products': product})
        else:
            usr = CustomeUser.objects.get(reff_code=ref)
            product = Product.objects.get(user=usr, id=id)
            disamount = (product.price * 10)/100
            print(disamount)
            total = product.price - disamount

            Cart.objects.create(product_name=product, status=1, user=usr,
                                amount=disamount, buy_user=request.user.username)

            messages.info(request, 'Product Added To Cart')
            return redirect('dash')
    except Exception as e:
        print(e)
        return HttpResponse("404 (Not Fount)")
