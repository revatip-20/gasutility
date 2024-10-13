# landing/models.py
from django.db import models

class ServiceRequest(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('Repair', 'Repair'),
        ('Installation', 'Installation'),
        ('Maintenance', 'Maintenance'),
        ('Other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    details = models.TextField()
    file = models.FileField(upload_to='service_requests/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Submitted')
    resolved_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service_type} request created on {self.created_at}"
