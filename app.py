from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
from models import db, User
from blueprints.main import main
from blueprints.admin import admin
import os

app = Flask(__name__)
app.config.from_object(Config)

# Ensure SECRET_KEY is set
if not app.config.get('SECRET_KEY'):
    app.config['SECRET_KEY'] = os.urandom(24).hex()

db.init_app(app)
bcrypt = Bcrypt(app)
app.bcrypt = bcrypt

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(main)
app.register_blueprint(admin, url_prefix='/admin')

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5003)