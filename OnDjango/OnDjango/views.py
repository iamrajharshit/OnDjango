from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    #return HttpResponse("We are working OnDjango")
    context={}
    return render(request,'website/index.html',context)

def contact(request):
    #return HttpResponse("Connect with me at @iamrajharshit")
    return render(request,'website/contact.html')