from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'posted_at')
    list_filter = ('job_type', 'location', 'category')
    search_fields = ('title', 'company', 'location')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'job', 'applied_at')
    list_filter = ('applied_at', 'job')
    search_fields = ('full_name', 'email', 'job__title')
