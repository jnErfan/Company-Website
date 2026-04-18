from app import app, db
from models import Company, Service, Portfolio, BlogPost, TeamMember, Testimonial

with app.app_context():
    # Add company info
    if not Company.query.first():
        company = Company(
            name="TechInnovate Solutions",
            description="We are a leading technology company specializing in innovative software solutions, web development, and digital transformation. Our team of experts is dedicated to delivering high-quality products that drive business success.",
            address="123 Innovation Drive, Tech City, TC 12345",
            phone="(555) 123-4567",
            email="info@techinnovate.com"
        )
        db.session.add(company)

    # Add services
    if not Service.query.first():
        services = [
            Service(
                title="Web Development",
                description="Custom web applications built with modern technologies. We create responsive, scalable, and secure web solutions tailored to your business needs.",
                image="web-dev.jpg"
            ),
            Service(
                title="Mobile App Development",
                description="Native and cross-platform mobile applications for iOS and Android. From concept to deployment, we handle the entire development lifecycle.",
                image="mobile-dev.jpg"
            ),
            Service(
                title="Cloud Solutions",
                description="Scalable cloud infrastructure and migration services. Optimize your operations with our cloud expertise on AWS, Azure, and Google Cloud.",
                image="cloud.jpg"
            )
        ]
        for service in services:
            db.session.add(service)

    # Add portfolio items
    if not Portfolio.query.first():
        portfolios = [
            Portfolio(
                title="E-Commerce Platform",
                description="A comprehensive e-commerce solution with payment integration, inventory management, and analytics dashboard.",
                image="ecommerce.jpg",
                link="https://example.com/ecommerce"
            ),
            Portfolio(
                title="Healthcare Management System",
                description="Secure patient management system with appointment scheduling, medical records, and telemedicine features.",
                image="healthcare.jpg",
                link="https://example.com/healthcare"
            ),
            Portfolio(
                title="Financial Dashboard",
                description="Real-time financial analytics platform with data visualization and reporting capabilities.",
                image="finance.jpg",
                link="https://example.com/finance"
            )
        ]
        for portfolio in portfolios:
            db.session.add(portfolio)

    # Add blog posts
    if not BlogPost.query.first():
        posts = [
            BlogPost(
                title="The Future of Web Development",
                content="<p>As technology evolves, web development continues to advance with new frameworks and tools. In this post, we explore the latest trends shaping the future of web development.</p><p>From progressive web apps to serverless architecture, developers have more options than ever. We'll discuss how these technologies can benefit your business.</p>",
                author="John Doe"
            ),
            BlogPost(
                title="Cybersecurity Best Practices",
                content="<p>In today's digital landscape, cybersecurity is paramount. Learn about essential best practices to protect your business from cyber threats.</p><p>From implementing multi-factor authentication to regular security audits, discover the steps you can take to safeguard your digital assets.</p>",
                author="Jane Smith"
            )
        ]
        for post in posts:
            db.session.add(post)

    # Add team members
    if not TeamMember.query.first():
        members = [
            TeamMember(
                name="Alice Johnson",
                position="CEO & Founder",
                bio="With over 15 years of experience in technology leadership, Alice founded TechInnovate to bring innovative solutions to businesses worldwide.",
                image="alice.jpg"
            ),
            TeamMember(
                name="Bob Wilson",
                position="CTO",
                bio="Bob leads our technical team with expertise in cloud architecture and software engineering. He holds multiple certifications in AWS and Azure.",
                image="bob.jpg"
            ),
            TeamMember(
                name="Carol Brown",
                position="Lead Developer",
                bio="Carol specializes in full-stack development and has worked on numerous high-profile projects. She's passionate about clean code and user experience.",
                image="carol.jpg"
            )
        ]
        for member in members:
            db.session.add(member)

    # Add testimonials
    if not Testimonial.query.first():
        testimonials = [
            Testimonial(
                name="David Lee",
                position="CEO, StartupXYZ",
                content="TechInnovate transformed our business with their innovative solutions. Their team's expertise and dedication are unmatched.",
                image="david.jpg"
            ),
            Testimonial(
                name="Emma Davis",
                position="CTO, CorpTech",
                content="Working with TechInnovate was a game-changer. They delivered a robust platform that exceeded our expectations.",
                image="emma.jpg"
            )
        ]
        for testimonial in testimonials:
            db.session.add(testimonial)

    db.session.commit()
    print("Sample data added successfully!")