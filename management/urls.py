from django.urls import path
from management.views import base,doctor,appointment,dental,physiotherapist,nuerology,gallery,home,succes





app_name = 'management'

urlpatterns=[
    path('',base,name='base'),
    path('doctor/',doctor,name='doctor'),
    path('appointment/',appointment,name='appointment'),
    path('dental/',dental,name='dental'),
    path('physiotherapist/',physiotherapist,name='physiotherapist'),
    path('nuerology/',nuerology,name='nuerology'),
    path('gallery/',gallery,name='gallery'),
    path('home/',home,name='home'),
    path('success/',succes,name='success')
    
    
]