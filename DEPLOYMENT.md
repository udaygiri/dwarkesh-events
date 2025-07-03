# Django Events App - Fly.io Deployment

This Django application is configured for deployment on Fly.io.

## Prerequisites

1. **Fly.io Account**: Sign up at [fly.io](https://fly.io)
2. **Payment Method**: Add a credit card to your Fly.io account (required for database creation)
3. **Fly CLI**: Already installed via the setup process

## Deployment Steps

### 1. Add Payment Information

Visit https://fly.io/dashboard/dwarkesheventes/billing and add a credit card.

### 2. Create PostgreSQL Database

```powershell
C:\Users\BAPU\.fly\bin\flyctl.exe postgres create --name dwarkesh-events-db --region iad
```

### 3. Launch the App

```powershell
C:\Users\BAPU\.fly\bin\flyctl.exe launch --no-deploy
```

### 4. Set Environment Variables

```powershell
# Generate and set a secret key
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set SECRET_KEY="your-generated-secret-key"
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set DEBUG=False

# Set database URL (get this from the postgres create step)
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set DATABASE_URL="postgresql://..."

# Set email configuration (optional)
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set EMAIL_HOST_USER="your-email@gmail.com"
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set EMAIL_HOST_PASSWORD="your-app-password"
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set DEFAULT_FROM_EMAIL="your-email@gmail.com"

# Set Cloudinary configuration (optional)
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set CLOUDINARY_CLOUD_NAME="your-cloud-name"
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set CLOUDINARY_API_KEY="your-api-key"
C:\Users\BAPU\.fly\bin\flyctl.exe secrets set CLOUDINARY_API_SECRET="your-api-secret"
```

### 5. Deploy

```powershell
C:\Users\BAPU\.fly\bin\flyctl.exe deploy
```

### 6. Run Migrations

```powershell
C:\Users\BAPU\.fly\bin\flyctl.exe ssh console -C "python manage.py migrate"
```

### 7. Create Superuser (Optional)

```powershell
C:\Users\BAPU\.fly\bin\flyctl.exe ssh console -C "python manage.py createsuperuser"
```

## Quick Deploy Script

You can also use the automated deployment script:

**Windows:**

```powershell
.\deploy.bat
```

**Linux/Mac:**

```bash
chmod +x deploy.sh
./deploy.sh
```

## Configuration Files

- `Dockerfile`: Container configuration
- `fly.toml`: Fly.io app configuration
- `.dockerignore`: Files to exclude from Docker build
- `.env.example`: Environment variables template

## Post-Deployment

Your app will be available at: `https://dwarkesh-events.fly.dev`

### Useful Commands

- **View logs**: `flyctl logs`
- **Scale app**: `flyctl scale count 2`
- **Open console**: `flyctl ssh console`
- **View app info**: `flyctl info`
- **View secrets**: `flyctl secrets list`

## Troubleshooting

1. **Build fails**: Check Dockerfile and requirements.txt
2. **Database connection fails**: Verify DATABASE_URL secret
3. **Static files not loading**: Ensure collectstatic runs in Dockerfile
4. **App won't start**: Check logs with `flyctl logs`

## Local Development

1. Copy `.env.example` to `.env`
2. Fill in your environment variables
3. Run: `python manage.py runserver`

## File Structure

```
├── Dockerfile              # Container configuration
├── fly.toml                # Fly.io configuration
├── .dockerignore           # Docker ignore file
├── deploy.sh/.bat          # Deployment scripts
├── requirements.txt        # Python dependencies
├── manage.py              # Django management script
├── dwarkeshevents/        # Django project
├── gallery/               # Gallery app
├── contact/               # Contact app
├── templates/             # HTML templates
└── static/                # Static files
```
