from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def base(request):
    return render(request,'base.html')
def doctor(request):
    return render(request,'doctor.html')
from django.shortcuts import render
from .models import Appointment  # Import the Appointment model

def appointment(request):
    if request.method == 'POST':
        patient_name = request.POST.get('patient_name')
        doctor = request.POST.get('doctor')
        date = request.POST.get('Date')
        time = request.POST.get('Time')
        mobile_number = request.POST.get('mobile_number')
        message = request.POST.get('message')
        print(doctor)
        print("---------------------------------------")
        print(mobile_number)
        print(date)
        # Check if the required fields are not empty before saving
            # Save the data to the Appointment model
        appointment = Appointment(patient_name=patient_name,doctor=doctor,date=date,time=time,mobile_number=mobile_number,message=message)
            # Optionally, you can also save the appointment instance to update the database
        appointment.save()
        
        
         # Create an error page to inform the user

    return render(request, 'appointment.html')

    
def dental(request):
    return render(request,'dental.html')
def physiotherapist(request):
    return render(request,'physiotherapist.html')
def nuerology(request):
    return render(request,'nuerology.html')    
def gallery(request):
    return render(request,'gallery.html') 
def home(request):
    return render(request,'home.html')
def succes(request):
    return render(request,'sucess.html')
          