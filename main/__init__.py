from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize SQLAlchemy and LoginManager
db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

# Function to create a Flask app
def create_app():
    # Create a Flask instance
    app = Flask(__name__, instance_relative_config=True, template_folder='../templates')

    # Set the secret key
    app.config['SECRET_KEY'] = 'Qazedcr,fvtgbyhn415'

    # Load configuration
    app.config.from_pyfile('config.py', silent=True)

    # Set the database URI and disable SQLALCHEMY_TRACK_MODIFICATIONS
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://coda415:Qwerty415!@localhost/frantz'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the app with the SQLAlchemy database
    db.init_app(app)

    # Initialize the app with the LoginManager
    login_manager.init_app(app)

    # Create all the necessary database tables
    with app.app_context():
        db.create_all()

    # Import and register blueprints
    from .views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .create_user_blueprint import create_user_blueprint
    app.register_blueprint(create_user_blueprint)

    from .JobRequestPage import job_request_page
    app.register_blueprint(job_request_page)

    from .JobRequestSubmission import job_request_submission
    app.register_blueprint(job_request_submission)

    from .open_positions_blueprint import open_positions_blueprint
    app.register_blueprint(open_positions_blueprint)

    from .position_detail_blueprint import position_detail_blueprint
    app.register_blueprint(position_detail_blueprint)

    from .dashboard import dashboard as dashboard_blueprint
    app.register_blueprint(dashboard_blueprint)

    from .employee_term_form import employeetermform_blueprint
    app.register_blueprint(employeetermform_blueprint)

    # Import and register the new application blueprint
    from .application_blueprint import application_blueprint
    app.register_blueprint(application_blueprint)


    # Return the created Flask app
    return app

# Import the necessary models
from main.models import (user, regionalmanagermasterlist, accountmanagermasterlist, evansville, bowlinggreen, elizabethtown, bloomington, clarksville, jobmasterlist, openpositionsroster, termemployeetable, applicants)
