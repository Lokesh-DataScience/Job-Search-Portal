from django.db import models

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Remote', 'Remote'),
        ('Internship', 'Internship'),
    ]
    JOB_CATEGORY_CHOICES = [
        ('Technology', 'Technology'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Education', 'Education'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
        ('Design', 'Design'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=150)

    company_website = models.URLField(
        max_length=300,
        blank=True,
        null=True
    )

    company_email = models.EmailField(
        max_length=254
    )

    company_phone = models.CharField(
    max_length=20,
    help_text="Include country code, e.g. +91XXXXXXXXXX"
    )

    location = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=JOB_CATEGORY_CHOICES)

    experience = models.CharField(
        max_length=100,
        choices=[
            ('Entry Level', 'Entry Level'),
            ('Mid Level', 'Mid Level'),
            ('Senior Level', 'Senior Level'),
            ('Executive', 'Executive'),
        ]
    )

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES
    )

    number_of_positions = models.PositiveIntegerField(
        default=1
    )

    salary_min = models.IntegerField()
    salary_max = models.IntegerField()

    application_deadline = models.DateField()

    description = models.TextField()

    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.company}"


class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    cover_letter = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application by {self.full_name} for {self.job.title}"
