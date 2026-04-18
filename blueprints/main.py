from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
from models import db, Service, Portfolio, BlogPost, TeamMember, Testimonial, ContactMessage, Company

main = Blueprint('main', __name__)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject')
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')

@main.route('/')
def home():
    company = Company.query.first()
    services = Service.query.limit(3).all()
    testimonials = Testimonial.query.limit(3).all()
    portfolio_items = Portfolio.query.limit(6).all()
    return render_template('index.html', company=company, services=services, testimonials=testimonials, portfolio_items=portfolio_items)

@main.route('/about')
def about():
    company = Company.query.first()
    team = TeamMember.query.all()
    return render_template('about.html', company=company, team=team)

@main.route('/services')
def services():
    services = Service.query.all()
    return render_template('services.html', services=services)

@main.route('/portfolio')
def portfolio():
    items = Portfolio.query.all()
    return render_template('portfolio.html', items=items)

@main.route('/team')
def team():
    members = TeamMember.query.all()
    return render_template('team.html', members=members)

@main.route('/testimonials')
def testimonials():
    testimonials = Testimonial.query.all()
    return render_template('testimonials.html', testimonials=testimonials)

@main.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)

@main.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('blog_post.html', post=post)

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(message)
        db.session.commit()
        flash('Your message has been sent!', 'success')
        return redirect(url_for('main.thank_you'))
    return render_template('contact.html', form=form)

@main.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

@main.route('/careers')
def careers():
    return render_template('careers.html')