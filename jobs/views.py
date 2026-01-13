from django.shortcuts import render, get_object_or_404
from .models import Job, JobApplication
from .forms import JobForm
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Count
from django.contrib.auth.decorators import login_required


def job_list(request):
    jobs = Job.objects.all().order_by('-posted_at')

    keyword = request.GET.get('keyword')
    location = request.GET.get('location')
    category = request.GET.get('category')
    job_type = request.GET.get('job_type')

    if keyword:
        jobs = jobs.filter(title__icontains=keyword)

    if location and location != "All Locations":
        jobs = jobs.filter(location__icontains=location)

    if category and category != "All Categories":
        jobs = jobs.filter(category__icontains=category)

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    # compute top companies for the slider (company name + job count)
    companies_qs = Job.objects.values('company').annotate(count=Count('id')).order_by('-count')[:8]
    companies = []
    ICON_MAP = {
        'google': 'fab fa-google',
        'microsoft': 'fab fa-microsoft',
        'apple': 'fab fa-apple',
        'amazon': 'fab fa-amazon',
        'meta': 'fab fa-facebook',
        'facebook': 'fab fa-facebook',
        'salesforce': 'fa-brands fa-salesforce',
    }

    for entry in companies_qs:
        name = entry['company'] or 'Unknown'
        slug = slugify(name)
        key = name.lower()
        icon_class = ICON_MAP.get(key, 'fas fa-briefcase')
        companies.append({'name': name, 'slug': slug, 'count': entry['count'], 'icon_class': icon_class})

    context = {
        'jobs': jobs,
        'companies': companies,
    }
    return render(request, 'jobs/job_list.html', context)

@login_required(login_url='/login/')
def post_job(request):
    if request.method == "POST":
        Job.objects.create(
            company=request.POST.get("company"),
            company_website=request.POST.get("company_website"),
            company_email=request.POST.get("company_email"),
            company_phone=request.POST.get("company_phone"),

            title=request.POST.get("title"),
            category=request.POST.get("category"),
            job_type=request.POST.get("job_type"),
            experience=request.POST.get("experience"),
            location=request.POST.get("location"),

            salary_min=request.POST.get("salary_min"),
            salary_max=request.POST.get("salary_max"),
            description=request.POST.get("description"),

            application_deadline=request.POST.get("application_deadline") or None,
            number_of_positions=request.POST.get("number_of_positions", 1),
        )
        return redirect("home")

    return render(request, "jobs/post_job.html")


@login_required(login_url='/login/')
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')

        # basic server-side validation
        if not full_name or not email or not resume:
            messages.error(request, 'Please provide name, email and a resume file.')
            return render(request, 'jobs/apply_job.html', {'job': job})

        if resume.size > 5 * 1024 * 1024:
            messages.error(request, 'Resume must be smaller than 5MB')
            return render(request, 'jobs/apply_job.html', {'job': job})

        application = JobApplication.objects.create(
            job=job,
            full_name=full_name,
            email=email,
            phone=phone or '',
            cover_letter=cover_letter or '',
            resume=resume,
        )

        messages.success(request, 'Application submitted — we will be in touch!')
        return redirect('home')

    return render(request, 'jobs/apply_job.html', {'job': job})


def google_jobs(request):
    """Render jobs for Google."""
    jobs = Job.objects.filter(company__icontains='google').order_by('-posted_at')
    return render(request, 'jobs/google_jobs.html', {'jobs': jobs})

def microsoft_jobs(request):
    """Render jobs for Microsoft."""
    jobs = Job.objects.filter(company__icontains='microsoft').order_by('-posted_at')
    return render(request, 'jobs/microsoft_jobs.html', {'jobs': jobs})

def apple_jobs(request):
    """Render jobs for apple."""
    jobs = Job.objects.filter(company__icontains='apple').order_by('-posted_at')
    return render(request, 'jobs/apple_jobs.html', {'jobs': jobs})

def amazon_jobs(request):
    """Render jobs for amazon."""
    jobs = Job.objects.filter(company__icontains='amazon').order_by('-posted_at')
    return render(request, 'jobs/amazon_jobs.html', {'jobs': jobs})

def meta_jobs(request):
    """Render jobs for meta."""
    jobs = Job.objects.filter(company__icontains='meta').order_by('-posted_at')
    return render(request, 'jobs/meta_jobs.html', {'jobs': jobs})

def salesforce_jobs(request):
    """Render jobs for salesforce."""
    jobs = Job.objects.filter(company__icontains='salesforce').order_by('-posted_at')
    return render(request, 'jobs/salesforce_jobs.html', {'jobs': jobs})