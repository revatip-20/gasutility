# landing/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ServiceRequestForm, RequestTrackingForm
from .models import ServiceRequest
import time

def landing_page(request):
    return render(request, 'landing_page.html')

def services_page(request):
    return render(request, 'services_page.html')

def submit_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'submit_request.html', {'form': form})

def request_success(request):
    return render(request, 'request_success.html')

def track_request(request):
    if request.method == 'POST':
        form = RequestTrackingForm(request.POST)
        if form.is_valid():
            # Redirect to status_request regardless of the request_id
            return redirect('status_request')
    else:
        form = RequestTrackingForm()
    return render(request, 'track_request.html', {'form': form})

# landing/views.py
def status_request(request):
    statuses = [
        "Request Submitted",
        "Request Reviewed",
        "Request Accepted",
        "Service Boy Allocated",
        "Service Boy Reaching",
    ]
    return render(request, 'status_request.html', {'statuses': statuses})