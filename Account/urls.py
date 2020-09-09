from django.urls import path
from Account.views import registration_view

urlpatterns = [
    path('register',registration_view,name="register")
]