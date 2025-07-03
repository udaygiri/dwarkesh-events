@echo off
REM Fly.io Deployment Script for Django (Windows)

echo 🚀 Starting Fly.io deployment process...

REM Step 1: Check if flyctl is installed
where flyctl >nul 2>nul
if %errorlevel% neq 0 (
    echo ❌ flyctl is not installed. Please install it first:
    echo PowerShell: iwr https://fly.io/install.ps1 -useb ^| iex
    exit /b 1
)

REM Step 2: Login to Fly.io (if not already logged in)
echo 🔐 Checking Fly.io authentication...
flyctl auth whoami >nul 2>nul
if %errorlevel% neq 0 (
    echo Please login to Fly.io:
    flyctl auth login
)

REM Step 3: Set environment variables
echo 🔧 Setting up environment variables...
for /f %%i in ('python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"') do set SECRET_KEY=%%i
flyctl secrets set SECRET_KEY=%SECRET_KEY%
flyctl secrets set DEBUG=False

REM Step 4: Deploy the application
echo 🚀 Deploying to Fly.io...
flyctl deploy

echo ✅ Deployment complete!
echo 🌐 Your app should be available at: https://dwarkesh-events.fly.dev

REM Step 5: Run database migrations (if database is set up)
echo 🗄️  Running database migrations...
flyctl ssh console -C "python manage.py migrate"

echo 🎉 All done! Your Django app is live on Fly.io!
