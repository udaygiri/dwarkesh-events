#!/bin/bash

# Fly.io Deployment Script for Django

echo "🚀 Starting Fly.io deployment process..."

# Step 1: Check if flyctl is installed
if ! command -v flyctl &> /dev/null; then
    echo "❌ flyctl is not installed. Please install it first:"
    echo "PowerShell: iwr https://fly.io/install.ps1 -useb | iex"
    exit 1
fi

# Step 2: Login to Fly.io (if not already logged in)
echo "🔐 Checking Fly.io authentication..."
if ! flyctl auth whoami &> /dev/null; then
    echo "Please login to Fly.io:"
    flyctl auth login
fi

# Step 3: Set environment variables
echo "🔧 Setting up environment variables..."
flyctl secrets set SECRET_KEY=$(python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())')
flyctl secrets set DEBUG=False

# Step 4: Deploy the application
echo "🚀 Deploying to Fly.io..."
flyctl deploy

echo "✅ Deployment complete!"
echo "🌐 Your app should be available at: https://dwarkesh-events.fly.dev"

# Step 5: Run database migrations (if database is set up)
echo "🗄️  Running database migrations..."
flyctl ssh console -C "python manage.py migrate"

echo "🎉 All done! Your Django app is live on Fly.io!"
