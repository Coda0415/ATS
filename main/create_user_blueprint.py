from flask import Blueprint, request, render_template
from .models import user, regionalmanagermasterlist, accountmanagermasterlist
from . import db
from sqlalchemy import func
import bcrypt

create_user_blueprint = Blueprint("create_user", __name__)


@create_user_blueprint.route("/create_user", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email").strip()
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if a user with the same email already exists
        existing_user = user.query.filter_by(email=email).first()
        if existing_user:
            return "A user with this email already exists.", 400

        print("Email entered:", email)
        manager_emails = [manager.manageremail for manager in db.session.query(regionalmanagermasterlist).all()]
        print("Manager emails:", manager_emails)

        # Check if the email matches against the regionalmanagermasterlist and accountmanagermasterlist tables
        regional_manager = regionalmanagermasterlist.query.filter(
            func.lower(regionalmanagermasterlist.manageremail) == func.lower(email)).first()
        if regional_manager:
            role = "RegionalManager"
            region = regional_manager.region
        else:
            account_manager = accountmanagermasterlist.query.filter(
                func.lower(accountmanagermasterlist.manageremail) == func.lower(email)).first()
            if account_manager:
                role = "AccountManager"
                region = account_manager.region
            else:
                role = "Admin"
                region = "All"

        if password == confirm_password:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            new_user = user(
                username=username,
                email=email,
                password=hashed_password,
                role=role,
                region=region
            )

            db.session.add(new_user)
            db.session.commit()

            return {"message": "User created successfully"}, 201
        else:
            return {"error": "Passwords do not match"}, 400

    return render_template("create_user.html")
