from django.urls import path
from printerNotice import views

urlpatterns = [
    path("", views.home, name="home"),
    path('home/', views.home, name="home"),
    path('signup/', views.Email_Signup, name="Email_Signup"),
    path('hello/<name>', views.hello_there, name="hello_there"),
]
