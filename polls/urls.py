from django.urls import path

from . import views

urlpattern = [path('',views.index, name = 'index'),
              ]


'''
the next step is to point the root URL conf at the polls.urls module in mywebsite/urls.py

'''