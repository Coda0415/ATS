from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from . import db
from .models import jobmasterlist
from flask_wtf import FlaskForm


job_request_page = Blueprint('job_request_page', __name__)

@login_required
@job_request_page.route("/JobRequestPage", methods=["GET", "POST"])
def job_request_form():
    form = FlaskForm()
    if not current_user.is_authenticated:
        return redirect(url_for("create_user.create_user"))

    if current_user.role not in ['RegionalManager', 'Admin']:
        abort(403, description="Access denied. You must be a Regional Manager or Admin to access this page.")

    user_region = current_user.region

    job_titles = ["Janitorial Cleaner", "Team Coordinator", "Team Lead", "Floor Tech"]

    try:
        if current_user.role == 'Admin':
            job_numbers = [{"JobNumber": job.jobnumber, "Region": job.region} for job in
                           db.session.query(jobmasterlist.jobnumber, jobmasterlist.region).all()]
        else:
            job_numbers = [{"JobNumber": job.jobnumber, "Region": job.region} for job in
                           db.session.query(jobmasterlist.jobnumber, jobmasterlist.region).filter(
                               jobmasterlist.region == user_region).all()]
    except Exception as e:
        return "Error: Could not retrieve job numbers from database.", 500

    question_data = [
        {"type": "MULTIPLE_CHOICE", "question": "Is this Position Full-Time or Part-Time?",
         "options": ["Full-Time", "Part-Time"]},
        {"type": "RADIO", "question": "Part-Time or Full-Time?", "options": ["Part-Time", "Full-Time"]},
        {"type": "TEXT", "question": "What is the hourly pay for this postion?"},
        {"type": "TIME", "question": "Shift Starting Time"},
        {"type": "TIME", "question": "Shift Ending Time"},
        {"type": "TEXT", "question": "Number of Hours this Job can Flex:"},
        {"type": "CHECKBOX", "question": "What Days does this Position work?",
         "options": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]},
        {"type": "TEXT", "question": "How many positions do you need to fill?"},
        {"type": "CHECKBOX", "question": "Select any Special Instructions:",
         "options": ["SOB", "Steel Toe Boots", "Safety Glasses", "Hard Had", "Able to Wear PPE",
                     "Floor Maintenance Experience", "MVR", "Drivers License", "Vaccination", "Vaccination Records",
                     "Lift Push Pull 50lbs for Whole Shift"]}

    ]

    regions = ["Bowling Green Region", "Evansville Region", "Clarksville Region", "Elizabethtown Region",
               "Bloomington Region"]

    return render_template("JobRequestPage.html", question_data=question_data, job_titles=job_titles,
                           job_numbers=job_numbers, user_role=current_user.role, regions=regions,form=form)
