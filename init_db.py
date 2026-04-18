from app import app, db, bcrypt
from models import User, Service, Portfolio, BlogPost, TeamMember, Testimonial, Company, ContactMessage
from datetime import datetime

with app.app_context():
    db.create_all()

    # Create or update admin user
    admin_user = User.query.filter_by(username='admin').first()
    if not admin_user:
        hashed_password = bcrypt.generate_password_hash('admin').decode('utf-8')
        admin = User(username='admin', email='admin@example.com', password=hashed_password, role='admin')
        db.session.add(admin)
        db.session.commit()
        print('Admin user created: username=admin, password=admin')
    else:
        # Update password and role if needed
        if not bcrypt.check_password_hash(admin_user.password, 'admin'):
            admin_user.password = bcrypt.generate_password_hash('admin').decode('utf-8')
        if not admin_user.role:
            admin_user.role = 'admin'
        db.session.commit()
        print('Admin user updated with correct password and role')

    # Create company info if it doesn't exist
    company = Company.query.first()
    if not company:
        company = Company(
            name='TechSolutions Inc.',
            description='Leading technology solutions provider specializing in web development, mobile apps, and digital transformation.',
            address='123 Business Street, Tech City, TC 12345',
            phone='+1 (555) 123-4567',
            email='info@techsolutions.com'
        )
        db.session.add(company)
        db.session.commit()
        print('Company info created')

    # Add sample services
    if Service.query.count() == 0:
        services_data = [
            {
                'title': 'Web Development',
                'description': 'Custom web applications built with modern technologies including React, Node.js, and cloud platforms. We create responsive, scalable, and secure web solutions tailored to your business needs.',
                'image': 'https://picsum.photos/400/300?random=1'
            },
            {
                'title': 'Mobile App Development',
                'description': 'Native and cross-platform mobile applications for iOS and Android. From concept to deployment, we deliver engaging mobile experiences that drive user engagement and business growth.',
                'image': 'https://picsum.photos/400/300?random=2'
            },
            {
                'title': 'Digital Marketing',
                'description': 'Comprehensive digital marketing strategies including SEO, social media marketing, content creation, and PPC campaigns. Drive traffic, increase conversions, and grow your online presence.',
                'image': 'https://picsum.photos/400/300?random=3'
            },
            {
                'title': 'Cloud Solutions',
                'description': 'Scalable cloud infrastructure and migration services. We help businesses leverage AWS, Azure, and Google Cloud for improved performance, security, and cost efficiency.',
                'image': 'https://picsum.photos/400/300?random=4'
            }
        ]

        for service_data in services_data:
            service = Service(**service_data)
            db.session.add(service)
        db.session.commit()
        print('Sample services added')

    # Add sample portfolio items
    if Portfolio.query.count() == 0:
        portfolio_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A complete e-commerce solution for a retail company with payment integration, inventory management, and customer analytics. Built with React and Node.js.',
                'image': 'https://picsum.photos/400/300?random=5',
                'link': 'https://example.com/portfolio/ecommerce'
            },
            {
                'title': 'Healthcare Management System',
                'description': 'Comprehensive healthcare management platform with patient records, appointment scheduling, and telemedicine features. HIPAA compliant and secure.',
                'image': 'https://picsum.photos/400/300?random=6',
                'link': 'https://example.com/portfolio/healthcare'
            },
            {
                'title': 'Financial Dashboard',
                'description': 'Real-time financial analytics dashboard for investment firms. Features include market data visualization, portfolio tracking, and automated reporting.',
                'image': 'https://picsum.photos/400/300?random=7',
                'link': 'https://example.com/portfolio/finance'
            },
            {
                'title': 'Learning Management System',
                'description': 'Online learning platform with course management, video streaming, progress tracking, and certification features. Used by educational institutions worldwide.',
                'image': 'https://picsum.photos/400/300?random=8',
                'link': 'https://example.com/portfolio/lms'
            }
        ]

        for item_data in portfolio_data:
            item = Portfolio(**item_data)
            db.session.add(item)
        db.session.commit()
        print('Sample portfolio items added')

    # Add sample blog posts
    if BlogPost.query.count() == 0:
        blog_data = [
            {
                'title': 'The Future of Web Development: Trends to Watch in 2024',
                'content': '''The web development landscape is constantly evolving, and staying ahead of the curve is crucial for businesses and developers alike. In this comprehensive guide, we'll explore the most significant trends shaping the future of web development.

## 1. Artificial Intelligence and Machine Learning Integration

AI is no longer just a buzzword—it's becoming an integral part of web applications. From chatbots that provide instant customer support to recommendation engines that personalize user experiences, AI is transforming how we build and interact with websites.

## 2. Progressive Web Apps (PWAs)

PWAs combine the best of web and mobile applications, offering native app-like experiences directly through the browser. With features like offline functionality, push notifications, and home screen installation, PWAs are bridging the gap between web and mobile experiences.

## 3. Serverless Architecture

Serverless computing allows developers to focus on writing code without worrying about server management. This approach offers better scalability, reduced costs, and faster development cycles.

## 4. WebAssembly for High-Performance Applications

WebAssembly (Wasm) enables high-performance applications to run in the browser. From gaming to complex data processing, WebAssembly is opening new possibilities for web-based applications.

The future of web development is exciting, with these trends promising more powerful, efficient, and user-friendly applications. Stay tuned for more insights on implementing these technologies in your projects.''',
                'author': 'Sarah Johnson'
            },
            {
                'title': 'Building Scalable Mobile Applications: Best Practices',
                'content': '''Creating mobile applications that can handle growing user bases and increasing feature demands requires careful planning and implementation. In this article, we'll discuss the key principles and best practices for building scalable mobile applications.

## Understanding Scalability

Scalability in mobile applications refers to the ability of an app to handle increased load, users, and features without compromising performance. It's not just about handling more users—it's about maintaining excellent user experience as your app grows.

## 1. Architecture Design

Choose the right architecture from the start. Consider using clean architecture, MVVM, or similar patterns that separate concerns and make your code more maintainable and testable.

## 2. Database Optimization

Efficient data storage and retrieval are crucial for scalable apps. Use appropriate database solutions, implement proper indexing, and consider data synchronization strategies for offline functionality.

## 3. API Design

Design RESTful or GraphQL APIs that can handle increased loads. Implement proper caching, rate limiting, and error handling to ensure reliability.

## 4. Performance Monitoring

Implement comprehensive monitoring and analytics to track app performance, identify bottlenecks, and make data-driven decisions for optimization.

## 5. Code Quality

Maintain high code quality with automated testing, code reviews, and continuous integration. This ensures that your app remains stable and maintainable as it scales.

By following these best practices, you can build mobile applications that not only meet current needs but also grow successfully with your business.''',
                'author': 'Michael Chen'
            },
            {
                'title': 'Cybersecurity in the Digital Age: Protecting Your Business',
                'content': '''In today's interconnected world, cybersecurity is no longer optional—it's essential. With cyber threats becoming increasingly sophisticated, businesses must prioritize security to protect their data, customers, and reputation.

## The Current Threat Landscape

Cyber attacks are on the rise, with ransomware, phishing, and data breaches affecting businesses of all sizes. Understanding the threats is the first step in building effective defenses.

## 1. Employee Training and Awareness

Your employees are often the first line of defense. Regular training on cybersecurity best practices, phishing recognition, and safe computing habits is crucial.

## 2. Multi-Factor Authentication (MFA)

Implement MFA across all systems and applications. This simple step can prevent a significant percentage of unauthorized access attempts.

## 3. Regular Security Audits

Conduct regular security assessments and penetration testing to identify vulnerabilities before attackers can exploit them.

## 4. Data Encryption

Encrypt sensitive data both at rest and in transit. This ensures that even if data is compromised, it remains unreadable to unauthorized parties.

## 5. Incident Response Planning

Develop and regularly update an incident response plan. Knowing how to react quickly and effectively to security incidents can minimize damage and recovery time.

## 6. Compliance and Regulations

Stay informed about relevant regulations like GDPR, CCPA, and industry-specific standards. Compliance not only protects your business legally but also guides security best practices.

Investing in cybersecurity is investing in your business's future. Don't wait for a breach to happen—proactive security measures are always more cost-effective than reactive ones.''',
                'author': 'David Rodriguez'
            },
            {
                'title': 'The Rise of Remote Work: Technology Solutions for Distributed Teams',
                'content': '''The global shift to remote work has transformed how we think about collaboration, productivity, and work-life balance. Technology plays a crucial role in making remote work successful, and understanding the right tools and strategies is key to building effective distributed teams.

## The Remote Work Revolution

Remote work is no longer a temporary arrangement—it's become a fundamental part of the modern workplace. Companies that embrace remote work effectively gain access to global talent pools and often see improvements in employee satisfaction and productivity.

## Essential Tools for Remote Teams

### Communication Platforms
- Slack or Microsoft Teams for instant messaging
- Zoom or Google Meet for video conferencing
- Email for formal communications

### Project Management
- Asana or Trello for task tracking
- Jira for complex project management
- Monday.com for customizable workflows

### Collaboration Tools
- Google Workspace or Microsoft 365 for document collaboration
- Figma for design collaboration
- GitHub for code collaboration

## Building Remote Work Culture

Successful remote work goes beyond tools—it's about culture. Companies need to focus on:

1. **Clear Communication**: Establish regular check-ins and transparent communication channels
2. **Trust and Autonomy**: Give team members the freedom to manage their time effectively
3. **Inclusive Practices**: Ensure all team members feel valued and included
4. **Work-Life Balance**: Respect boundaries between work and personal time

## Security Considerations

Remote work introduces new security challenges. Implement VPNs, secure authentication, and regular security training to protect company data.

## Measuring Success

Track key metrics like productivity, employee satisfaction, and retention rates to ensure your remote work strategy is effective.

The future of work is distributed, and companies that adapt successfully will thrive in this new paradigm. By leveraging the right technology and fostering a supportive culture, remote work can be a win for both employers and employees.''',
                'author': 'Emma Thompson'
            }
        ]

        for post_data in blog_data:
            post = BlogPost(**post_data)
            db.session.add(post)
        db.session.commit()
        print('Sample blog posts added')

    # Add sample team members
    if TeamMember.query.count() == 0:
        team_data = [
            {
                'name': 'Sarah Johnson',
                'position': 'Chief Technology Officer',
                'bio': 'Sarah brings over 15 years of experience in software development and technology leadership. She specializes in scalable architecture and has led multiple successful digital transformation projects.',
                'image': 'https://picsum.photos/300/300?random=9'
            },
            {
                'name': 'Michael Chen',
                'position': 'Lead Developer',
                'bio': 'Michael is a full-stack developer with expertise in modern web technologies. He has a passion for clean code and user experience, having built applications serving millions of users.',
                'image': 'https://picsum.photos/300/300?random=10'
            },
            {
                'name': 'David Rodriguez',
                'position': 'Security Specialist',
                'bio': 'David is our cybersecurity expert with a background in ethical hacking and security auditing. He ensures all our solutions meet the highest security standards and compliance requirements.',
                'image': 'https://picsum.photos/300/300?random=11'
            },
            {
                'name': 'Emma Thompson',
                'position': 'UX/UI Designer',
                'bio': 'Emma creates beautiful, intuitive user experiences that delight users and drive business results. Her designs have been featured in design publications and won multiple industry awards.',
                'image': 'https://picsum.photos/300/300?random=12'
            }
        ]

        for member_data in team_data:
            member = TeamMember(**member_data)
            db.session.add(member)
        db.session.commit()
        print('Sample team members added')

    # Add sample testimonials
    if Testimonial.query.count() == 0:
        testimonial_data = [
            {
                'name': 'John Smith',
                'position': 'CEO, TechCorp',
                'content': 'TechSolutions transformed our online presence completely. Their team delivered a modern, scalable platform that has increased our conversion rates by 150%. The attention to detail and technical expertise is outstanding.',
                'image': 'https://picsum.photos/100/100?random=13'
            },
            {
                'name': 'Maria Garcia',
                'position': 'Marketing Director, GrowthCo',
                'content': 'Working with TechSolutions was a game-changer for our digital marketing efforts. They not only built us a beautiful website but also implemented advanced analytics that helped us understand our customers better.',
                'image': 'https://picsum.photos/100/100?random=14'
            },
            {
                'name': 'Robert Kim',
                'position': 'Founder, StartupXYZ',
                'content': 'As a startup founder, I needed a development partner I could trust. TechSolutions delivered beyond expectations - on time, on budget, and with exceptional quality. They\'ve been instrumental in our growth.',
                'image': 'https://picsum.photos/100/100?random=15'
            },
            {
                'name': 'Lisa Anderson',
                'position': 'IT Manager, Enterprise Solutions',
                'content': 'The mobile app TechSolutions developed for us has revolutionized how our field teams work. The intuitive design and robust functionality have significantly improved our operational efficiency.',
                'image': 'https://picsum.photos/100/100?random=16'
            }
        ]

        for testimonial_data_item in testimonial_data:
            testimonial = Testimonial(**testimonial_data_item)
            db.session.add(testimonial)
        db.session.commit()
        print('Sample testimonials added')

    # Add sample contact messages
    if ContactMessage.query.count() == 0:
        contact_data = [
            {
                'name': 'Alice Brown',
                'email': 'alice.brown@email.com',
                'subject': 'Website Development Inquiry',
                'message': 'Hi, I\'m interested in developing a new website for my business. Could you please provide more information about your web development services and pricing?'
            },
            {
                'name': 'Tom Wilson',
                'email': 'tom.wilson@company.com',
                'subject': 'Mobile App Consultation',
                'message': 'We\'re looking to develop a mobile application for our customers. I\'d like to schedule a consultation to discuss our requirements and explore possible solutions.'
            },
            {
                'name': 'Jennifer Lee',
                'email': 'j.lee@startup.io',
                'subject': 'Partnership Opportunity',
                'message': 'I represent a growing startup and we\'re looking for technology partners. Your portfolio looks impressive and I\'d like to discuss potential collaboration opportunities.'
            }
        ]

        for contact_data_item in contact_data:
            contact = ContactMessage(**contact_data_item)
            db.session.add(contact)
        db.session.commit()
        print('Sample contact messages added')

    print('Database initialization complete!')