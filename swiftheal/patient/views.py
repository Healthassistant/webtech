from django.shortcuts import render,redirect
from patient.models import Patient

def home(request):
    if('patient' in request.session):
        patientdetails=Patient.objects.get(Patient_AdharId=request.session['patient'])
        parameters={"name":patientdetails.Name}
        return render(request,'profilePage.html',parameters)
    else:
        return redirect('home')

def signup(request):
    if(request.method=='POST'):
        AadharId=request.POST['aadharID']
        Phone=request.POST['phone']
        Name=request.POST['name']
        Age=request.POST['age']
        Gender=request.POST['gender']
        State=request.POST['state']
        Address=request.POST['address']
        Pin=request.POST['pin']
        try:
            patientdetails=Patient(Patient_AdharId=AadharId,Mobile_no=Phone,Name=Name,Age=Age,Gender=Gender,State=State,Address=Address,Pincode=Pin)
            patientdetails.save()
            request.session['patient']=AadharId
            return redirect('patient_home')
        except Exception as e:
            return redirect('home')
    return redirect('home')





