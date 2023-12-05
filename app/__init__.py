from flask import Flask
from .database.db import db
from config import Config
from .routes import product_routes, user_routes, auth_routes, product_views_routes
from flask_jwt_extended import JWTManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

mail = Mail(app)

with app.app_context():
    db.create_all()

app.register_blueprint(product_routes.product_blueprint)
app.register_blueprint(user_routes.user_blueprint)
app.register_blueprint(auth_routes.auth_blueprint)
app.register_blueprint(product_views_routes.product_views_blueprint)
