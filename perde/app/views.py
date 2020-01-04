from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *


def index(request):
    template_name = "app/index.html"
    return render(request, template_name, {})


def register(request):
    template_name = "app/register.html"
    return render(request, template_name, {})


def site_login(request):
    template_name = "app/login.html"
    return render(request, template_name, {})


def site_logout(request):
    logout(request)
    return redirect("app:index")


def create_order(request):
    template_name = "app/create_order.html"
    if request.user.is_authenticated:
        context = {}
        orders = Order.objects.filter(user=request.user, status=0).order_by('-pk')
        provinces = Province.objects.all()
        context["provinces"] = provinces
        if len(orders):
            order = orders[0]
            products = Product.objects.filter(order=order)
            context["order"] = order
            context["products"] = products
        else:
            order = Order()
            order.user = request.user
            order.status = 0
            order.save()
        if request.method == "POST":
            type = request.POST.get("type")
            if type == "add_product":
                image = request.FILES["image"]
                description = request.POST.get("description")

                product = Product()
                product.order = order
                product.image = image
                product.description = description
                product.save()
            elif type == "delete_product":
                Product.objects.filter(id=request.POST.get("productid")).delete()
        return render(request, template_name, context)
    else:
        return redirect("app:index")


@csrf_exempt
def get_districts(request):
    template_name = "parts/districts.html"
    provinceid = request.POST.get("pid")
    print(provinceid)
    districts = District.objects.filter(province__id=provinceid)
    return render(request, template_name, {"districts": districts})

