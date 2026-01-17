# Render Deployment Guide

This Django project is configured for deployment on **Render**.

## Prerequisites

- GitHub account with this repository pushed
- Render account (render.com)
- Python 3.11+

## Step-by-Step Deployment

### 1. Push Your Code to GitHub
```bash
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### 2. Create a New Web Service on Render

1. Go to [render.com](https://render.com) and sign in
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Fill in the details:
   - **Name**: `job-search-engine` (or your preferred name)
   - **Environment**: `Python 3`
   - **Region**: Choose closest to your users
   - **Branch**: `main` (or your branch)
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput`
   - **Start Command**: `gunicorn job_search_engine.wsgi:application`

### 3. Configure Environment Variables

In Render dashboard, go to **Environment** section and add:

```
DEBUG=False
SECRET_KEY=<your-unique-secret-key>
ALLOWED_HOSTS=<your-app-name>.onrender.com
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

**⚠️ Important**: Generate a secure SECRET_KEY using:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 4. (Optional) Add PostgreSQL Database

1. In Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure database settings
3. Render will automatically set `DATABASE_URL` environment variable
4. Update `settings.py` to use PostgreSQL (see section below)

### 5. Deploy

Click the **"Deploy"** button. Render will:
- Clone your repository
- Install dependencies from `requirements.txt`
- Run migrations (from `Procfile` release phase)
- Collect static files
- Start your app with gunicorn

## Static Files

Static files are automatically served by:
- **WhiteNoise middleware** (configured in settings.py)
- Compressed for better performance

No additional static file hosting needed!

## Database Options

### Option A: SQLite (Current - Not Recommended for Production)
Works but has limitations on Render's ephemeral filesystem.

### Option B: PostgreSQL (Recommended)
1. Add PostgreSQL database in Render dashboard
2. Update `requirements.txt`:
   ```
   psycopg2-binary==2.9.9
   ```
3. Update `settings.py` `DATABASES` section:
   ```python
   import dj_database_url
   
   DATABASES = {
       'default': dj_database_url.config(
           default='sqlite:///db.sqlite3',
           conn_max_age=600
       )
   }
   ```
4. Add to `requirements.txt`:
   ```
   dj-database-url==2.1.0
   ```

## Troubleshooting

### Application crashes on startup
- Check **Logs** in Render dashboard
- Ensure all migrations ran: Check "Events" tab
- Verify environment variables are set correctly

### Static files not loading (404 errors)
- Run `python manage.py collectstatic --noinput` locally to test
- Verify `STATIC_ROOT` is set in settings.py
- Clear Render cache and redeploy

### Database connection errors
- Verify `DATABASE_URL` environment variable is set
- Check PostgreSQL is running if using Render PostgreSQL
- Run migrations via Render shell:
  ```bash
  render exec python manage.py migrate
  ```

### 403 Forbidden errors
- Update `ALLOWED_HOSTS` in environment variables
- Include your exact Render domain (e.g., `my-app.onrender.com`)

## Monitoring

- **Logs**: View real-time logs in Render dashboard
- **Metrics**: Monitor CPU, memory, and requests
- **Health Checks**: Render automatically monitors your app

## Custom Domain

1. In Render, go to **Settings** → **Custom Domain**
2. Add your domain
3. Update DNS records as instructed
4. Update `ALLOWED_HOSTS` environment variable

## Cost & Resources

- **Free Tier**: 0.5 CPU, 512 MB RAM (spins down after 15 min inactivity)
- **Paid Tier**: Dedicated resources, always running

## Useful Commands

Run commands on Render using the shell:

```bash
# View all users
render exec python manage.py shell

# Create superuser
render exec python manage.py createsuperuser

# Run migrations
render exec python manage.py migrate

# Collect static files
render exec python manage.py collectstatic
```

## Security Checklist

- ✅ DEBUG = False
- ✅ SECRET_KEY changed from default
- ✅ ALLOWED_HOSTS configured
- ✅ HTTPS enabled (SECURE_SSL_REDIRECT = True)
- ✅ Cookie security enabled
- ✅ WhiteNoise serves static files
- ⏳ Consider adding database backups
- ⏳ Set up monitoring/alerts
