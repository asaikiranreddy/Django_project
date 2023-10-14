# timetable_app/views.py
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Course, Timetable
import random
from django.shortcuts import render
import pandas as pd
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import RegistrationForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        last_two_digits = request.POST.get('last_two_digits')

        # Check if the last two digits of the entered password match the actual password
        if password.endswith(last_two_digits):
            # Perform user authentication and other logic here
            # ...
            return HttpResponseRedirect('home')  # Redirect after successful login
        else:
            error_message = 'Incorrect Secret key '
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def user_registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to a protected page after successful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# views.py

import pandas as pd
import random
from django.shortcuts import render
from .models import Subject

def timetable_generator(request):
    # Replace this with the path to your Excel file
    excel_file_path = "C:\\Users\\anire\\Downloads\\H SECTION.xlsx"

    # Load subjects from Excel sheet
    subjects_df = pd.read_excel(excel_file_path)
    subjects_list = subjects_df['Subject'].tolist()

    # Example timetable_data
    timetable_data = [
        {'Day_Time': 'Monday'},
        {'Day_Time': 'Tuesday'},
        {'Day_Time': 'Wednesday'},
        {'Day_Time': 'Thursday'},
        {'Day_Time': 'Friday'},
        {'Day_Time': 'Saturday'},
    ]

    # Allocate subjects randomly to each day
    for day in timetable_data:
        day['Subjects'] = random.sample(subjects_list, len(subjects_list))

    # Render the timetable_generator.html template with the generated data
    return render(request, 'registration/timetable_generator.html', {'timetable_data': timetable_data})


import random

def generate_timetable(subjects):
    # Example logic to generate a simple timetable
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    times = ['9:00-9:55', '9:55-10:50', '10:50-11:45', '11:45-12:40 PM', '12:40 PM-1:20 PM', '1:20-2:15', '2:15-3:10', '3:10-4:05']

    timetable_data = []

    subject_index = 0  # Initialize index for subject selection

    for day in days:
        day_data = {'Day_Time': day}

        for time in times:
            # Skip subject allocation for the 12:40 PM-1:20 PM time slot
            if time == '12:40 PM-1:20 PM':
                subject = ''
            else:
                # Use a round-robin approach to select subjects
                subject = subjects[subject_index]
                subject_index = (subject_index + 1) % len(subjects)

            day_data[time.replace(':', '_')] = subject

        timetable_data.append(day_data)

    return timetable_data

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        last_two_digits = request.POST.get('last_two_digits')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)

            # Redirect to the timetable generator page
            return redirect('timetable_generator')
        else:
            error_message = 'Invalid credentials. Please try again.'
            return render(request, 'registration/login.html', {'error_message': error_message})

    return render(request, 'registration/login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})



def user_logout(request):
    logout(request)
    return redirect('home')

def about_view(request):
    # You can add any context data you want to pass to the template here
    context = {
        'title': 'About Us',
        'content': 'This is the about page content.',
    }

    return render(request, 'about.html', context)

