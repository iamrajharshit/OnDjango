from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("We are working OnDjango")
    context={}
    return render(request,'index.html',context)

def contact(request):
    return HttpResponse("Connect with me at @iamrajharshit")
