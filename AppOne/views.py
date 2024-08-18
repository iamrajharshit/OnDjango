from django.shortcuts import render

# Create your views here.
def appone(request):
    return render(request, 'AppOne/app_html.html')