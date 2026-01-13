from django.urls import path
from .views import job_list, post_job, apply_job, google_jobs, microsoft_jobs, apple_jobs, amazon_jobs, meta_jobs, salesforce_jobs

urlpatterns = [
    path('', job_list, name='home'),
    path('post-job/', post_job, name='post_job'),
    path('jobs/<int:job_id>/apply/', apply_job, name='apply_job'),
    path('google/', google_jobs, name='google_jobs'),
    path('microsoft/', microsoft_jobs, name='microsoft_jobs'),
    path('apple/', apple_jobs, name='apple_jobs'),
    path('amazon/', amazon_jobs, name='amazon_jobs'),
    path('meta/', meta_jobs, name='meta_jobs'),
    path('salesforce/', salesforce_jobs, name='salesforce_jobs'),
]