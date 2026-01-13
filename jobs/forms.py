from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title',
            'company',
            'company_website',
            'company_email',
            'location',
            'category',
            'job_type',
            'number_of_positions',
            'salary_min',
            'salary_max',
            'application_deadline',
            'description',
        ]
