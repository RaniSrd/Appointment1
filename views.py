from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse # type: ignore

from models1 import Appointment # type: ignore
from .models import * # type: ignore
from django.contrib import messages # type: ignore
from django.contrib.auth.hashers import make_password, check_password # type: ignore
from django.db import IntegrityError # type: ignore
from datetime import date
from django.urls import get_resolver # type: ignore
from datetime import datetime
import calendar

# ============================home=================================



# ===============================================================================================
# def appointments(request):
#     if request.method == 'POST':
#         data = request.POST
#         appointment_date = data.get('appointment_date')
#         appointment_time = data.get('appointment_time')
#         person_name = data.get('lastName')
#         person_dob=data.get('brithdate')
#         person_phone = data.get('mobileNo')
#         person_email = data.get('person_email')
#         remarks=data.get('highestQualification')
#         meet_person_name=data.get('meet_person_name')
#         created_at=data.get('created_at')

#         # username = data.get('username')
#         # password = data.get('password')
#         # encrypted_Password = make_password(password)

#         # superuser = 1
#         # status = 0

#         context={
#             'appointment_date' : appointment_date,
#             'appointment_time' : appointment_time,
#             'person_name' : person_name,
#             'person_dob':person_dob,
#             'person_phone' : person_phone,
#             'person_email' : person_email,
#             'remarks' : remarks,
#             'meet_person_name' : meet_person_name,
#             'created_at': created_at,
#         }

#         # if Users.objects.filter(username=username).exists() and Users.objects.filter(email=email).exists():
#         #     messages.error(request, 'User already exist')
#         #     return render(request, 'Authentication/register.html',context)
#         # elif Users.objects.filter(username=username).exists():
#         #     messages.error(request, f'Username {username} not available',context)
#         #     return render(request, 'Authentication/register.html',context)
#         # elif Users.objects.filter(email=person_email).exists():
#         #     messages.error(request, 'Email id already exist')
#         #     return render(request, 'Authentication/register.html',context)

#         candidateId = Candidate.objects.create(
#             appointment_date=appointment_date,
#             appointment_time=appointment_time,
#             person_name=person_name,
#             person_dob=person_dob,
#             remarks = remarks,
#             meet_person_name=meet_person_name,
           
#         ).id

#         usertypeId=Usertype.objects.get(usertype_name="Candidate").id

#         # Users.objects.create(
#         #     username=username,
#         #     person_email=person_email,
#         #     password=encrypted_Password,
#         #     userid=candidateId,
#         #     superuser=superuser,
#         #     status=status,
#         #     usertypeid=usertypeId,
#         #     companyid=1,
#         # )

#         # user_id = Users.objects.get(email=email).id
#         Contact.objects.create(
#             appointment_date=appointment_date,
#             appointment_time=appointment_time,
#             person_name=person_name,
#             person_phone=person_phone,
#             person_email=person_email,
#             candidateid=candidateId,
#         )
#         return redirect('/login/')

#     return render(request, 'appointment.html')
#===================================================================================
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Appointments

# def appointment(request):
#     if request.method == 'POST':
#         data = request.POST
#         appointment_date = data.get('appointment_date')
#         appointment_time = data.get('appointment_time')
#         person_name = data.get('person_name')  
#         person_dob = data.get('person_dob')  
#         person_phone = data.get('person_phone')
#         person_email = data.get('person_email')
#         remarks = data.get('remarks')
#         meet_person_name = data.get('meet_person_name')

#         # Save data to the database
#         appointment = Appointments.objects.create(
#             appointment_date=appointment_date,
#             appointment_time=appointment_time,
#             person_name=person_name,
#             person_dob=person_dob,
#             person_phone=person_phone,
#             person_email=person_email,
#             remarks=remarks,
#             meet_person_name=meet_person_name,
#         )

#         messages.success(request, "Appointment booked successfully!")
#         return redirect('/index/')  # Redirect to a confirmation page

#     return render(request, 'index.html')  # Render the form


def appointment(request):
    if request.method == 'POST':
        data = request.POST
        appointment_date = data.get('appointment_date')
        appointment_time = data.get('appointment_time')
        person_name = data.get('person_name')  
        person_dob = data.get('person_dob')  
        person_phone = data.get('person_phone')
        person_email = data.get('person_email')
        remarks = data.get('remarks')
        meet_person_name = data.get('meet_person_name')

        # Validate and convert date format
        try:
            appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()
        except ValueError:
            messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")
            return redirect('/index/')  # Redirect to the form page with an error

        # Save data to the database
        appointment = Appointment.objects.create(
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            person_name=person_name,
            person_dob=person_dob,
            person_phone=person_phone,
            person_email=person_email,
            remarks=remarks,
            meet_person_name=meet_person_name,
        )

        messages.success(request, "Appointment booked successfully!")
        return redirect('/index/')  # Redirect to a confirmation page

    return render(request, 'index.html')



# def appointment(request):
#     if request.method == 'POST':
#         try:
#             appointment_date = request.POST.get('appointment_date')
#             appointment_date = datetime.strptime(appointment_date, '%Y-%m-%d').date()  # Ensure correct format
            
#             appointment_time = request.POST.get('appointment_time')
#             person_name = request.POST.get('person_name')
#             person_dob = request.POST.get('person_dob')
#             person_dob = datetime.strptime(person_dob, '%Y-%m-%d').date()  # Convert DOB
#             person_phone = request.POST.get('person_phone')
#             person_email = request.POST.get('person_email')
#             meet_person_name = request.POST.get('meet_person_name')
#             remarks = request.POST.get('remarks')

#             # Save to database
#             appointment = Appointments.objects.create(
#                 appointment_date=appointment_date,
#                 appointment_time=appointment_time,
#                 person_name=person_name,
#                 person_dob=person_dob,
#                 person_phone=person_phone,
#                 person_email=person_email,
#                 meet_person_name=meet_person_name,
#                 remarks=remarks
#             )
#             appointment.save()
#             messages.success(request, "Appointment created successfully!")
#             return redirect('appointment_success')  # Redirect after successful submission

#         except ValueError:
#             messages.error(request, "Invalid date format. Please use YYYY-MM-DD.")

#     return render(request, 'appointment.html')

# ===========================================


# =========================================================================