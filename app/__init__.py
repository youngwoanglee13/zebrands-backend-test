from flask import Flask
from .database.db import db
from config import Config
from .routes import product_routes, user_routes, auth_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(product_routes.product_blueprint)
app.register_blueprint(user_routes.user_blueprint)
app.register_blueprint(auth_routes.auth_blueprint)
