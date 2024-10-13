# landing/forms.py
from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['service_type', 'details', 'file']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 4}),
        }
class RequestTrackingForm(forms.Form):
    request_id = forms.IntegerField(label='Request ID')