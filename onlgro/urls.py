from django.urls import path,include
from .import views

urlpatterns = [
path('',views.TestFun,name='test'),
path('contact',views.TestFuncont,name='contact'),
path('contact1',views.newpg,name='contact1')
]