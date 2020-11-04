from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('SignUp', views.signup, name='SignUp'),
    path('handlesignup', views.handlesignup, name='handlesignup'),
    path('handlesignin', views.handlesignin, name='handlesignin'),
    path('Logout', views.Logout, name='Logout'),
    path('Rescue',views.Rescue, name='Resue'),
    path('handleRescue',views.handleRescue, name='handleRescue'),
    path('feedback',views.feedback, name='feedback'),

]