# Company Website

A complete, professional company website built with Flask, featuring comprehensive content, responsive design, and advanced UI elements.

## Features

- **Complete Public Pages**: Home (hero, services, portfolio, testimonials), About (company info + team), Services, Portfolio, Team, Testimonials, Blog, Contact, Careers
- **Advanced Design**: Modern Bootstrap 5 styling with gradients, shadows, animations, and smooth scrolling
- **Interactive Elements**: Hover effects, scroll animations, form validation, and responsive navigation
- **Rich Content**: Detailed descriptions, statistics, social links, and professional imagery
- **Contact System**: Functional contact form with database storage and thank-you page
- **Admin Dashboard**: Full CRUD interface for managing all content types
- **Database**: SQLite with comprehensive models and sample data
- **Authentication**: Secure admin login with password hashing
- **Responsive Layout**: Mobile-first design that works on all devices

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Initialize database and add sample data**:
   ```bash
   python init_db.py
   python populate_db.py
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the website**:
   - Main site: http://127.0.0.1:5000
   - Admin panel: http://127.0.0.1:5000/admin/login (admin/admin)

## Sample Data Included

- Company information with contact details
- 3 sample services (Web Dev, Mobile Dev, Cloud Solutions)
- 3 portfolio projects with external links
- 2 blog posts with rich content
- 3 team members with bios
- 2 customer testimonials
- Professional placeholder images throughout

## Project Structure

```
company-website/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── models.py             # Database models
├── init_db.py            # Database initialization
├── populate_db.py        # Sample data population
├── requirements.txt      # Python dependencies
├── Procfile              # Heroku deployment
├── render.yaml           # Render deployment
├── blueprints/           # Route organization
│   ├── main.py          # Public routes
│   └── admin.py         # Admin routes
├── templates/            # Jinja2 templates
│   ├── base.html        # Base layout
│   ├── index.html       # Home page
│   ├── about.html       # About page
│   ├── services.html    # Services page
│   ├── portfolio.html   # Portfolio page
│   ├── team.html        # Team page
│   ├── testimonials.html # Testimonials page
│   ├── blog.html        # Blog listing
│   ├── blog_post.html   # Individual blog post
│   ├── contact.html     # Contact page
│   ├── thank_you.html   # Contact success
│   ├── careers.html     # Careers page
│   └── admin/           # Admin templates
├── static/               # Static assets
│   ├── css/
│   │   └── style.css    # Custom styles
│   ├── js/
│   │   └── script.js    # Interactive features
│   └── images/          # Image assets
└── README.md            # This file
```

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Forms**: Flask-WTF
- **Authentication**: Flask-Login + Bcrypt
- **Deployment**: Ready for Heroku/Render

## Customization

- **Content**: Edit via admin panel or directly in database
- **Styling**: Modify `static/css/style.css`
- **Images**: Replace placeholder URLs with your own images
- **Functionality**: Extend blueprints in `blueprints/`

## Deployment

- **Heroku**: Use `Procfile`
- **Render**: Use `render.yaml`
- Set environment variables: `SECRET_KEY`, `DATABASE_URL` (for production)

The website is now production-ready with professional design, comprehensive content, and smooth user experience!