from django.shortcuts import render,redirect
from doctor.models import Doctor

def homes(request):
    if('doctor' in request.session):
        doctordetails=Doctor.objects.get(Doctor_id=request.session['doctor'])
        parameters={"name":doctordetails.Name}
        return render(request,'profilePage.html',parameters)
    else:
        return redirect('home')

