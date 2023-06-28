from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from flask_login import current_user
from .models import db, accountmanagermasterlist, regionalmanagermasterlist, jobmasterlist, employeemasterlist, termemployeetable
import json
employeetermform_blueprint = Blueprint("employeetermform", __name__)


@employeetermform_blueprint.route('/get_job_numbers')
def get_job_numbers():
    # Get email and role from the current user
    user_email = current_user.email
    user_role = current_user.role
    manager_name = None

    # Check if the user is an AccountManager or RegionalManager and get the corresponding manager name
    if user_role == 'AccountManager':
        manager = accountmanagermasterlist.query.filter_by(manageremail=user_email).first()
        if manager:
            manager_name = manager.accountmanager
    elif user_role == 'RegionalManager':
        manager = regionalmanagermasterlist.query.filter_by(manageremail=user_email).first()
        if manager:
            manager_name = manager.regionalmanager

    # Fetch job numbers based on the manager name and role
    if manager_name:
        if user_role == 'AccountManager':
            jobs = jobmasterlist.query.filter_by(accountmanager=manager_name).all()
        elif user_role == 'RegionalManager':
            jobs = jobmasterlist.query.filter_by(regionalmanager=manager_name).all()

        job_numbers = [{"JobNumber": job.jobnumber, "Region": job.region} for job in jobs]
    else:
        job_numbers = []

    return jsonify(job_numbers=job_numbers)

@employeetermform_blueprint.route('/get_employee_names/<job_number>')
def get_employee_names(job_number):
    # Get the job name from the jobmasterlist table based on the job_number
    job = jobmasterlist.query.filter_by(jobnumber=job_number).first()
    job_name = job.jobname if job else None


    # Get all the employees from employeemasterlist that have the specified job name
    if job_name:
        employees = employeemasterlist.query.filter_by(jobname=job_name).all()
    else:
        employees = []

    employee_names = [{"id": employee.id, "name": f"{employee.firstname} {employee.lastname}", "employee_number": employee.employeenumber} for employee in employees]
    print("Job Name:", job_name)
    return jsonify({'employee_names': employee_names, 'job_name': job_name})





@employeetermform_blueprint.route("/employeetermform", methods=["GET", "POST"])
def employeetermform():
    if request.method == "POST":
        # TODO: Process the submitted form data and save it to the database
        pass
    job_number = request.args.get('job_number')
    team_member_name = request.args.get('team_member_name')
    employee_number = request.args.get('employee_number')
    jobname= request.args.get('jobname')
    return render_template('employeetermform.html', job_number=job_number,
                           team_member_name=team_member_name, employee_number=employee_number, jobname=jobname)


@employeetermform_blueprint.route("/submit_employeetermform", methods=["POST"])
def submit_employeetermform():
    employee_number = request.form.get('employee_number')
    employees = employeemasterlist.query.filter_by(employeenumber=employee_number).all()

    if employees:
        for employee in employees:
            employee_data = {
                'id': employee.id,
                'employeenumber': employee.employeenumber,
                'firstname': employee.firstname,
                'lastname': employee.lastname,
                'hiredate': employee.hiredate,
                'classificationdescription': employee.classificationdescription,
                'employeetypedescription': employee.employeetypedescription,
                'supervisordescription': employee.supervisordescription,
                'jobnumber': employee.jobnumber,
                'jobname': employee.jobname,
                'categorydescription': employee.categorydescription,
                'region': employee.region,
                'title': employee.title,
                'jobstate': employee.jobstate,
                'companyaddress2': employee.companyaddress2,
                'uctaxpayeridnumber': employee.uctaxpayeridnumber,
                'jobaddress': employee.jobaddress,
                'jobaddress2': employee.jobaddress2,
                'jobcity': employee.jobcity,
                'jobzip': employee.jobzip,
                'employmenttype': employee.employmenttype,
                'lastdayworked': request.form.get('last_day_worked'),
                'reasonforleaving': request.form.get('reason_for_leaving'),
                'additionalinformation': request.form.get('additional_information'),
                'dependabilityslider': request.form.get('dependability_slider'),
                'dependabilitycomments': request.form.get('dependability_comments'),
                'abilityslider': request.form.get('ability_slider'),
                'abilitycomments': request.form.get('ability_comments'),
                'attitudetowardjobslider': request.form.get('attitude_toward_job_slider'),
                'attitudetowardjobcomments': request.form.get('attitude_toward_job_comments'),
                'attitudetowardsupervisorslider': request.form.get('attitude_toward_supervisor_slider'),
                'attitudetowardsupervisorcomments': request.form.get('attitude_toward_supervisor_comments'),
                'attitudetowardcoworkersslider': request.form.get('attitude_toward_co-workers_slider'),
                'attitudetowardcoworkerscomments': request.form.get('attitude_toward_co-workers_comments'),
                'leadershipslider': request.form.get('leadership_slider'),
                'leadershipcomments': request.form.get('leadership_comments'),
                'workwithoutsupervisionslider': request.form.get('work_without_supervision_slider'),
                'workwithoutsupervisioncomments': request.form.get('work_without_supervision_comments'),
                'totalevalscore': '',  # Add the appropriate form data for 'totalevalscore'
                'eligibleforhire': '',  # Add the appropriate form data for 'eligibleforhire'
                'eligibleforhiredate': ''  # Add the appropriate form data for 'eligibleforhiredate'
            }

            term_employee = termemployeetable(**employee_data)

            # Add the new instance to the session
            db.session.add(term_employee)

            # Delete employee from employeemasterlist
            db.session.delete(employee)

            print("Added to term employee table and deleted from master list: ", employee_data['employeenumber'])

        # Commit the transaction
        db.session.commit()
        return redirect(url_for('dashboard.dashboard_view'))
    else:
        return "Employee not Found"


@employeetermform_blueprint.route("/add_to_employeemasterlist", methods=["POST"])
def add_to_employeemasterlist():
    # Read employee data from the JSON file
    with open('termedemployee.json', 'r') as file:
        employee_data = json.load(file)

    # Create a new employee record in employeemasterlist
    new_employee = employeemasterlist(
        id=employee_data['id'],
        employeenumber=employee_data['employeenumber'],
        firstname=employee_data['firstname'],
        lastname=employee_data['lastname'],
        hiredate=employee_data['hiredate'],
        classificationdescription=employee_data['classificationdescription'],
        employeetypedescription=employee_data['employeetypedescription'],
        supervisordescription=employee_data['supervisordescription'],
        categorydescription=employee_data['categorydescription'],
        region=employee_data['region'],
        title=employee_data['title'],
        companyaddress2=employee_data['companyaddress2'],
        uctaxpayeridnumber=employee_data['uctaxpayeridnumber'],
        employmenttype=employee_data['employmenttype'],
        jobnumber=employee_data['jobnumber'],
        jobname=employee_data['jobname'],
        jobstate=employee_data['jobstate'],
        jobaddress=employee_data['jobaddress'],
        jobaddress2=employee_data['jobaddress2'],
        jobcity=employee_data['jobcity'],
        jobzip=employee_data['jobzip']
    )

    # Add the new employee to the session and commit changes
    db.session.add(new_employee)
    db.session.commit()

    return redirect(url_for("employeetermform.employeetermform"))