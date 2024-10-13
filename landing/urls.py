# landing/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('services/', views.services_page, name='services_page'),
    path('submit-request/', views.submit_request, name='submit_request'),
    path('request-success/', views.request_success, name='request_success'),
    path('track-request/', views.track_request, name='track_request'),
    path('status-request/', views.status_request, name='status_request'),  # No request_id needed
]
