from django.urls import path


#localhost:8000/appone/next
from . import views
urlpatterns = [
    path('',views.appone, name='AppOne'),
    # path('order/',views.order,name='order')
    ]
