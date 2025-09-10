from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Makeup, User, Booking, Inquiry, Service
from django.utils import timezone

def index(request):
    return render(request, 'index.html')

def makeup(request):
    makeups = Makeup.objects.all()
    return render(request, 'makeup.html', {'makeups': makeups})

def booking(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Please login to make a booking.')
            return redirect('login')

        makeup_id = request.POST.get('makeup_id')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')
        location = request.POST.get('location')
        special_requests = request.POST.get('special_requests')

        try:
            makeup_obj = Makeup.objects.get(id=makeup_id)
            booking = Booking.objects.create(
                user=request.user,
                makeup=makeup_obj,
                event_date=event_date,
                event_time=event_time,
                location=location,
                special_requests=special_requests,
                total_price=makeup_obj.price
            )
            messages.success(request, 'Booking created successfully!')
            return redirect('booking')
        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')

    services = Service.objects.filter(is_active=True)
    return render(request, 'booking.html', {'services': services})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'show_login_popup': True})
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone_number = request.POST.get('phone_number')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                phone_number=phone_number
            )
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')

    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('index')

def inquire(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        event_date = request.POST.get('event_date')

        try:
            inquiry = Inquiry(
                name=name,
                email=email,
                phone_number=phone_number,
                message=message,
                event_date=event_date if event_date else None
            )
            inquiry.save()
            messages.success(request, 'Inquiry submitted successfully! We will contact you soon.')
            return redirect('inquire')
        except Exception as e:
            messages.error(request, f'Error submitting inquiry: {str(e)}')

    return render(request, 'inquire.html')

# New API view to provide makeup data
def makeup_data(request):
    makeups = Makeup.objects.all()
    data = []
    for makeup in makeups:
        data.append({
            "id": makeup.id,
            "name": makeup.name,
            "type": makeup.type,
            "numericPrice": float(makeup.price),
            "price": f"₹{makeup.price}",
            "description": makeup.description,
            "image": makeup.image.url if makeup.image else "https://via.placeholder.com/300x180?text=No+Image",
            "special": "deals" if makeup.is_special_deal else ("award" if makeup.is_award_winner else "")
        })
    return JsonResponse(data, safe=False)

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
