# ClassyKicks - Django E-commerce Project

A Django-based e-commerce platform for selling shoes and footwear.

## Features

- Product listing and details
- User authentication
- Brand management
- Contact form
- Responsive design with Tailwind CSS
- Cloudinary integration for media storage

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables (create a `.env` file):
   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment on Render

### Prerequisites

1. A Render account
2. Git repository with your code

### Deployment Steps

1. **Connect your repository to Render:**
   - Go to your Render dashboard
   - Click "New +" and select "Web Service"
   - Connect your GitHub/GitLab repository

2. **Configure the service:**
   - **Name:** `classykicks` (or your preferred name)
   - **Environment:** `Python`
   - **Build Command:** 
     ```bash
     pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
     ```
   - **Start Command:** `gunicorn ClassyKicks.wsgi:application`

3. **Set Environment Variables:**
   - `SECRET_KEY`: Generate a secure Django secret key
   - `DEBUG`: `False`
   - `DATABASE_URL`: Will be automatically provided by Render
   - `CLOUD_NAME`: Your Cloudinary cloud name (optional)
   - `CLOUDINARY_API_KEY`: Your Cloudinary API key (optional)
   - `CLOUDINARY_API_SECRET`: Your Cloudinary API secret (optional)

4. **Database Setup:**
   - Create a PostgreSQL database in Render
   - The `DATABASE_URL` will be automatically set

### Environment Variables

Create these environment variables in your Render dashboard:

```
SECRET_KEY=your-generated-secret-key
DEBUG=False
DATABASE_URL=postgresql://user:password@host:port/database
CLOUD_NAME=your-cloudinary-cloud-name
CLOUDINARY_API_KEY=your-cloudinary-api-key
CLOUDINARY_API_SECRET=your-cloudinary-api-secret
```

### Troubleshooting

1. **Static files not loading:**
   - Ensure `STATIC_ROOT` is set correctly
   - Run `python manage.py collectstatic` during build

2. **Database connection issues:**
   - Check if `DATABASE_URL` is set correctly
   - Ensure PostgreSQL is running

3. **Media files not working:**
   - Set up Cloudinary credentials
   - Or configure local media serving

4. **500 Internal Server Error:**
   - Check Render logs for specific error messages
   - Ensure all required environment variables are set

### File Structure

```
ClassyKicks/
├── ClassyKicks/          # Django project settings
├── store/               # Main app
├── static/              # Static files
├── media/               # Media files
├── templates/           # Templates
├── requirements.txt     # Python dependencies
├── Procfile            # Render deployment config
├── render.yaml         # Render configuration
└── manage.py           # Django management script
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License. 