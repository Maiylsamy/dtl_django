from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    x = 10
    y =20
    z = [1,2,3,4,5,6]
    names = ["maiyl","suresh","harish"]
    scores = [{"maiyl":100,"mani":200},{"viji":300,"velan":400}]
    data = {"x":x ,"y":y,"z":z,"names":names,"scores":scores}
    return render(request,"dtl.html",data)


