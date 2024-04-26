from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return render(request,"about.html")

def role(request):
    return render(request,"role.html")


def home1(request):
    return render(request,"home 1.html")