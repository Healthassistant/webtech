from django.urls import path
from patient import views


urlpatterns = [
    path('p',views.home,name="patient_home"),
    path('signup',views.signup,name="patient_signup")
]