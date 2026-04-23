from django.shortcuts import render,redirect
from django.http import HttpResponse
from app.models import Doctor,patient
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
import joblib
import numpy as np
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    return render(request, 'home.html')

def doc(request):
    if request.method=='POST':
        n=request.POST['doctor_name']
        s=request.POST['specialization']
        data=Doctor(doctor_name=n,specialization=s)
        data.save()
        return render(request,'index.html',{'key':Doctor.objects.all()})
    return render(request,'index.html')

@login_required
def formm(request):
    if request.method == 'POST':
        n = request.POST['patient_name']
        a = int(request.POST['age'])
        dd = request.POST['appointment_date']
        d = request.POST['doctor_name']
        if a<10:
            return HttpResponse("inavlid Age")
        else:
            doc_obj = Doctor.objects.get(id=d)

            patient.objects.create(patient_name=n, age=a,appointment_date=dd, doctor=doc_obj)
            return render(request, 'form.html', {'success': True, 'Doctor': Doctor.objects.all()})

    return render(request, 'form.html', {'Doctor': Doctor.objects.all()})


def patient_management(request):
    doctors = Doctor.objects.all()
    doctor_id = request.GET.get('doctor')

    if doctor_id:
        data = patient.objects.filter(doctor_id=doctor_id)
    else:
        data = patient.objects.all()

    return render(request, 'patient_management.html', {
        'data': data,
        'doctors': doctors
    })


def delete_patient(request, id):
    patient.objects.get(id=id).delete()
    return redirect('patient_management')


def patientregister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        
        if User.objects.filter(username=username).exists():
            return HttpResponse("User already exists")
        else:
            User.objects.create_user(username=username, password=password)
            return redirect('patientlogin')
    return render(request, 'patientregister.html') 


def patientlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user: 
            auth_login(request,user)
            return redirect('formm')
        else:
            return HttpResponse("Invalid Credentials")  
    return render(request, 'patientlogin.html')

def logout(request):
    auth_logout(request)
    return redirect('home')

def check_diabetes(request):
    result = None
    if request.method == 'POST':
        try:
            # Extract form values
            pregnancies = float(request.POST['Pregnancies'])
            glucose = float(request.POST['Glucose'])
            blood_pressure = float(request.POST['BloodPressure'])
            skin_thickness = float(request.POST['SkinThickness'])
            insulin = float(request.POST['Insulin'])
            bmi = float(request.POST['BMI'])
            dpf = float(request.POST['DiabetesPedigreeFunction'])
            age = float(request.POST['Age'])
            
            # Form features array for model
            features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
            
            # Load the model - looking in the base directory
            model_path = os.path.join(settings.BASE_DIR, 'diabetes_model.pkl')
            model = joblib.load(model_path)
            
            # Make prediction
            prediction = model.predict(features)
            
            # Assuming 1 means Diabetic and 0 means Non-Diabetic
            if prediction[0] == 1:
                result = "The model predicts that the patient HAS DIABETES."
            else:
                result = "The model predicts that the patient DOES NOT HAVE DIABETES."
                
        except Exception as e:
            result = f"Error during prediction: {str(e)}. Please ensure 'diabetes_model.pkl' is in the main project folder along with manage.py"
            
    return render(request, 'check_diabetes.html', {'result': result})
