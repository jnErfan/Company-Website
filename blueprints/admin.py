from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user, login_required
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email
from models import db, User, Service, Portfolio, BlogPost, TeamMember, Testimonial, ContactMessage, Company

admin = Blueprint('admin', __name__)

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ServiceForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image Filename')
    submit = SubmitField('Submit')

class PortfolioForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = StringField('Image Filename')
    link = StringField('Link')
    submit = SubmitField('Submit')

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    author = StringField('Author')
    submit = SubmitField('Submit')

class TeamMemberForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    bio = TextAreaField('Bio')
    image = StringField('Image Filename')
    submit = SubmitField('Submit')

class TestimonialForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    position = StringField('Position')
    content = TextAreaField('Content', validators=[DataRequired()])
    image = StringField('Image Filename')
    submit = SubmitField('Submit')

class CompanyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    address = StringField('Address')
    phone = StringField('Phone')
    email = StringField('Email', validators=[Email()])
    submit = SubmitField('Submit')

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password')
    role = StringField('Role', validators=[DataRequired()])
    submit = SubmitField('Submit')

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and current_app.bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        else:
            flash('Login unsuccessful. Please check username and password', 'danger')
    return render_template('admin/login.html', form=form)

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@admin.route('/')
@login_required
def dashboard():
    # Get statistics
    services_count = Service.query.count()
    portfolio_count = Portfolio.query.count()
    blog_count = BlogPost.query.count()
    team_count = TeamMember.query.count()
    testimonials_count = Testimonial.query.count()
    contacts_count = ContactMessage.query.count()

    # Get recent items
    recent_contacts = ContactMessage.query.order_by(ContactMessage.date_sent.desc()).limit(5).all()
    recent_blog_posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).limit(3).all()

    return render_template('admin/dashboard.html',
                         services_count=services_count,
                         portfolio_count=portfolio_count,
                         blog_count=blog_count,
                         team_count=team_count,
                         testimonials_count=testimonials_count,
                         contacts_count=contacts_count,
                         recent_contacts=recent_contacts,
                         recent_blog_posts=recent_blog_posts)

# Services
@admin.route('/services')
@login_required
def services():
    services = Service.query.all()
    return render_template('admin/services.html', services=services)

@admin.route('/service/new', methods=['GET', 'POST'])
@login_required
def new_service():
    form = ServiceForm()
    if form.validate_on_submit():
        service = Service(title=form.title.data, description=form.description.data, image=form.image.data)
        db.session.add(service)
        db.session.commit()
        flash('Service added!', 'success')
        return redirect(url_for('admin.services'))
    return render_template('admin/service_form.html', form=form, legend='New Service')

@admin.route('/service/<int:service_id>', methods=['GET', 'POST'])
@login_required
def edit_service(service_id):
    service = Service.query.get_or_404(service_id)
    form = ServiceForm()
    if form.validate_on_submit():
        service.title = form.title.data
        service.description = form.description.data
        service.image = form.image.data
        db.session.commit()
        flash('Service updated!', 'success')
        return redirect(url_for('admin.services'))
    elif request.method == 'GET':
        form.title.data = service.title
        form.description.data = service.description
        form.image.data = service.image
    return render_template('admin/service_form.html', form=form, legend='Edit Service')

@admin.route('/service/<int:service_id>/delete', methods=['POST'])
@login_required
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    flash('Service deleted!', 'success')
    return redirect(url_for('admin.services'))

# Portfolio
@admin.route('/portfolio')
@login_required
def portfolio():
    items = Portfolio.query.all()
    return render_template('admin/portfolio.html', items=items)

@admin.route('/portfolio/new', methods=['GET', 'POST'])
@login_required
def new_portfolio():
    form = PortfolioForm()
    if form.validate_on_submit():
        item = Portfolio(title=form.title.data, description=form.description.data, image=form.image.data, link=form.link.data)
        db.session.add(item)
        db.session.commit()
        flash('Portfolio item added!', 'success')
        return redirect(url_for('admin.portfolio'))
    return render_template('admin/portfolio_form.html', form=form, legend='New Portfolio Item')

@admin.route('/portfolio/<int:item_id>', methods=['GET', 'POST'])
@login_required
def edit_portfolio(item_id):
    item = Portfolio.query.get_or_404(item_id)
    form = PortfolioForm()
    if form.validate_on_submit():
        item.title = form.title.data
        item.description = form.description.data
        item.image = form.image.data
        item.link = form.link.data
        db.session.commit()
        flash('Portfolio item updated!', 'success')
        return redirect(url_for('admin.portfolio'))
    elif request.method == 'GET':
        form.title.data = item.title
        form.description.data = item.description
        form.image.data = item.image
        form.link.data = item.link
    return render_template('admin/portfolio_form.html', form=form, legend='Edit Portfolio Item')

@admin.route('/portfolio/<int:item_id>/delete', methods=['POST'])
@login_required
def delete_portfolio(item_id):
    item = Portfolio.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Portfolio item deleted!', 'success')
    return redirect(url_for('admin.portfolio'))

# Blog Posts
@admin.route('/blog')
@login_required
def blog():
    posts = BlogPost.query.all()
    return render_template('admin/blog.html', posts=posts)

@admin.route('/blog/new', methods=['GET', 'POST'])
@login_required
def new_blog_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data, author=form.author.data)
        db.session.add(post)
        db.session.commit()
        flash('Blog post added!', 'success')
        return redirect(url_for('admin.blog'))
    return render_template('admin/blog_form.html', form=form, legend='New Blog Post')

@admin.route('/blog/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    form = BlogPostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.author = form.author.data
        db.session.commit()
        flash('Blog post updated!', 'success')
        return redirect(url_for('admin.blog'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
        form.author.data = post.author
    return render_template('admin/blog_form.html', form=form, legend='Edit Blog Post')

@admin.route('/blog/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Blog post deleted!', 'success')
    return redirect(url_for('admin.blog'))

# Team Members
@admin.route('/team')
@login_required
def team():
    members = TeamMember.query.all()
    return render_template('admin/team.html', members=members)

@admin.route('/team/new', methods=['GET', 'POST'])
@login_required
def new_team_member():
    form = TeamMemberForm()
    if form.validate_on_submit():
        member = TeamMember(name=form.name.data, position=form.position.data, bio=form.bio.data, image=form.image.data)
        db.session.add(member)
        db.session.commit()
        flash('Team member added!', 'success')
        return redirect(url_for('admin.team'))
    return render_template('admin/team_form.html', form=form, legend='New Team Member')

@admin.route('/team/<int:member_id>', methods=['GET', 'POST'])
@login_required
def edit_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    form = TeamMemberForm()
    if form.validate_on_submit():
        member.name = form.name.data
        member.position = form.position.data
        member.bio = form.bio.data
        member.image = form.image.data
        db.session.commit()
        flash('Team member updated!', 'success')
        return redirect(url_for('admin.team'))
    elif request.method == 'GET':
        form.name.data = member.name
        form.position.data = member.position
        form.bio.data = member.bio
        form.image.data = member.image
    return render_template('admin/team_form.html', form=form, legend='Edit Team Member')

@admin.route('/team/<int:member_id>/delete', methods=['POST'])
@login_required
def delete_team_member(member_id):
    member = TeamMember.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    flash('Team member deleted!', 'success')
    return redirect(url_for('admin.team'))

# Testimonials
@admin.route('/testimonials')
@login_required
def testimonials():
    testimonials = Testimonial.query.all()
    return render_template('admin/testimonials.html', testimonials=testimonials)

@admin.route('/testimonial/new', methods=['GET', 'POST'])
@login_required
def new_testimonial():
    form = TestimonialForm()
    if form.validate_on_submit():
        testimonial = Testimonial(name=form.name.data, position=form.position.data, content=form.content.data, image=form.image.data)
        db.session.add(testimonial)
        db.session.commit()
        flash('Testimonial added!', 'success')
        return redirect(url_for('admin.testimonials'))
    return render_template('admin/testimonial_form.html', form=form, legend='New Testimonial')

@admin.route('/testimonial/<int:testimonial_id>', methods=['GET', 'POST'])
@login_required
def edit_testimonial(testimonial_id):
    testimonial = Testimonial.query.get_or_404(testimonial_id)
    form = TestimonialForm()
    if form.validate_on_submit():
        testimonial.name = form.name.data
        testimonial.position = form.position.data
        testimonial.content = form.content.data
        testimonial.image = form.image.data
        db.session.commit()
        flash('Testimonial updated!', 'success')
        return redirect(url_for('admin.testimonials'))
    elif request.method == 'GET':
        form.name.data = testimonial.name
        form.position.data = testimonial.position
        form.content.data = testimonial.content
        form.image.data = testimonial.image
    return render_template('admin/testimonial_form.html', form=form, legend='Edit Testimonial')

@admin.route('/testimonial/<int:testimonial_id>/delete', methods=['POST'])
@login_required
def delete_testimonial(testimonial_id):
    testimonial = Testimonial.query.get_or_404(testimonial_id)
    db.session.delete(testimonial)
    db.session.commit()
    flash('Testimonial deleted!', 'success')
    return redirect(url_for('admin.testimonials'))

# Contact Messages
@admin.route('/contacts')
@login_required
def contacts():
    messages = ContactMessage.query.order_by(ContactMessage.date_sent.desc()).all()
    return render_template('admin/contacts.html', messages=messages)

@admin.route('/contact/<int:message_id>/delete', methods=['POST'])
@login_required
def delete_contact(message_id):
    message = ContactMessage.query.get_or_404(message_id)
    db.session.delete(message)
    db.session.commit()
    flash('Contact message deleted!', 'success')
    return redirect(url_for('admin.contacts'))

# Company
@admin.route('/company', methods=['GET', 'POST'])
@login_required
def edit_company():
    company = Company.query.first()
    if not company:
        company = Company()
        db.session.add(company)
        db.session.commit()
    form = CompanyForm()
    if form.validate_on_submit():
        company.name = form.name.data
        company.description = form.description.data
        company.address = form.address.data
        company.phone = form.phone.data
        company.email = form.email.data
        db.session.commit()
        flash('Company info updated!', 'success')
        return redirect(url_for('admin.dashboard'))
    elif request.method == 'GET':
        form.name.data = company.name
        form.description.data = company.description
        form.address.data = company.address
        form.phone.data = company.phone
        form.email.data = company.email
    return render_template('admin/company_form.html', form=form, legend='Edit Company Info')

# User Management
@admin.route('/users')
@login_required
def users():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('admin.dashboard'))
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@admin.route('/user/new', methods=['GET', 'POST'])
@login_required
def new_user():
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('admin.dashboard'))
    form = UserForm()
    if form.validate_on_submit():
        hashed_password = current_app.bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, role=form.role.data)
        db.session.add(user)
        db.session.commit()
        flash('User added!', 'success')
        return redirect(url_for('admin.users'))
    return render_template('admin/user_form.html', form=form, legend='New User')

@admin.route('/user/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('admin.dashboard'))
    user = User.query.get_or_404(user_id)
    form = UserForm()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        if form.password.data:
            user.password = current_app.bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.role = form.role.data
        db.session.commit()
        flash('User updated!', 'success')
        return redirect(url_for('admin.users'))
    elif request.method == 'GET':
        form.username.data = user.username
        form.email.data = user.email
        form.role.data = user.role
    return render_template('admin/user_form.html', form=form, legend='Edit User')

@admin.route('/user/<int:user_id>/delete', methods=['POST'])
@login_required
def delete_user(user_id):
    if current_user.role != 'admin':
        flash('Access denied. Admin privileges required.', 'danger')
        return redirect(url_for('admin.dashboard'))
    if user_id == current_user.id:
        flash('You cannot delete your own account!', 'danger')
        return redirect(url_for('admin.users'))
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted!', 'success')
    return redirect(url_for('admin.users'))