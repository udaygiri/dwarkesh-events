# Vercel Deployment Instructions

## Prerequisites

1. Install Vercel CLI: `npm i -g vercel`
2. Create a Vercel account at https://vercel.com

## Deployment Steps

### 1. Login to Vercel

```bash
vercel login
```

### 2. Deploy to Vercel

```bash
vercel --prod
```

### 3. Set Environment Variables

After deployment, set these environment variables in Vercel dashboard:

**Required:**

- `SECRET_KEY` = your-secret-key
- `DEBUG` = False
- `DJANGO_SETTINGS_MODULE` = dwarkeshevents.settings

**For Cloudinary (Media Storage):**

- `CLOUDINARY_CLOUD_NAME` = dqkgzzmkr
- `CLOUDINARY_API_KEY` = 762694757195965
- `CLOUDINARY_API_SECRET` = scbWa9j0BuvZsU2SEOTBYQIfpBo

**For Database (Optional - uses SQLite by default):**

- `DATABASE_URL` = your-database-url (PostgreSQL, MySQL, etc.)

**For Email (Optional):**

- `EMAIL_HOST` = smtp.gmail.com
- `EMAIL_PORT` = 587
- `EMAIL_USE_TLS` = True
- `EMAIL_HOST_USER` = your-email@gmail.com
- `EMAIL_HOST_PASSWORD` = your-app-password
- `DEFAULT_FROM_EMAIL` = your-email@gmail.com

### 4. Access Your App

Your app will be available at: `https://your-project-name.vercel.app`

## Notes

- Vercel automatically detects changes in your GitHub repo and redeploys
- Static files are served by Vercel's CDN
- Media files are stored in Cloudinary
- Database can be SQLite (for testing) or external PostgreSQL/MySQL

## Troubleshooting

- Check Vercel dashboard for deployment logs
- Ensure all environment variables are set correctly
- Verify `vercel.json` configuration is correct
