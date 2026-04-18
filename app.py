from flask import Flask
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
from models import db, User
from blueprints.main import main
from blueprints.admin import admin

app = Flask(__name__)
app.config.from_object(Config)

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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5003)