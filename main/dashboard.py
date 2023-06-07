from flask import Blueprint, render_template, request
from flask_login import current_user
from .models import jobmasterlist, accountmanagermasterlist, regionalmanagermasterlist, employeemasterlist, openpositionsroster, applicants as Applicant
from datetime import datetime

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

manager_name = None

def get_manager_jobs(manager_name):
    jobs = jobmasterlist.query.filter(jobmasterlist.accountmanager.contains(manager_name)).all()
    return jobs

def get_open_positions(manager_name):
    open_positions = openpositionsroster.query.filter_by(accountmanager=manager_name).all()
    return open_positions

def get_user_accounts():
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            manager = accountmanagermasterlist.query.filter(accountmanagermasterlist.manageremail.ilike(current_user.email)).first()
            if manager:
                return jobmasterlist.query.filter(jobmasterlist.accountmanager.contains(manager.accountmanager)).all()
        elif current_user.role == 'RegionalManager':
            manager = regionalmanagermasterlist.query.filter(regionalmanagermasterlist.manageremail.ilike(current_user.email)).first()
            if manager:
                return jobmasterlist.query.filter(jobmasterlist.regionalmanager.contains(manager.regionalmanager)).all()
    return []


@dashboard.route('/dashboard', methods=['GET'])
def dashboard_view():
    global manager_name
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
            if manager:
                manager_name = manager.accountmanager
                jobs = get_manager_jobs(manager_name)
                accounts = get_user_accounts()
                return render_template('dashboard.html', jobs=jobs, accounts=accounts, selected_menu='employees')
        elif current_user.role == 'RegionalManager':
            manager_name = None  # Reset the manager_name for regional managers
            accounts = get_user_accounts()
            return render_template('dashboard.html', accounts=accounts, selected_menu='employees')
    return render_template('login.html')

@dashboard.route('/dashboard/<menu>', methods=['GET'])
def dashboard_view_menu(menu):
    global manager_name
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            if menu == 'employees':
                manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
                if manager:
                    manager_name = manager.accountmanager
                    jobs = get_manager_jobs(manager_name)
                    accounts = get_user_accounts()
                    return render_template('dashboard.html', jobs=jobs, accounts=accounts, selected_menu='employees')
            elif menu == 'open_positions':
                manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
                if manager:
                    manager_name = manager.accountmanager
                    jobs = get_manager_jobs(manager_name)
                    accounts = get_user_accounts()
                    open_positions = get_open_positions(manager_name)
                    return render_template('dashboard.html', jobs=jobs, accounts=accounts, open_positions=open_positions, selected_menu='open_positions')
            elif menu == 'applicants':
                manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
                print(manager.accountmanager)
                if manager:
                    manager_name = manager.accountmanager
                    jobs = get_manager_jobs(manager_name)
                    accounts = get_user_accounts()
                    applicants = Applicant.query.filter_by(accountmanager=manager_name).all()
                    print(manager_name)
                    print(True)
                    return render_template('dashboard.html', jobs=jobs, accounts=accounts, all_applicants=applicants, selected_menu='applicants')
            else:
                # Redirect to a relevant page or return an error message
                return render_template('error.html', message='Invalid menu option')
        elif current_user.role == 'RegionalManager':
            manager_name = None  # Reset the manager_name for regional managers
            accounts = get_user_accounts()
            if menu == 'employees':
                return render_template('dashboard.html', accounts=accounts, selected_menu='employees')
            elif menu == 'open_positions':
                manager = regionalmanagermasterlist.query.filter(regionalmanagermasterlist.manageremail.ilike(current_user.email)).first()
                print(manager.regionalmanager)
                if manager:
                    manager_name = manager.regionalmanager
                    open_positions = openpositionsroster.query.filter_by(regionalmanager=manager_name).all()
                    return render_template('dashboard.html', accounts=accounts, open_positions=open_positions, selected_menu='open_positions')
            elif menu == 'applicants':
                manager = regionalmanagermasterlist.query.filter(regionalmanagermasterlist.manageremail.ilike(current_user.email)).first()
                print(manager.regionalmanager)
                if manager:
                    manager_name = manager.regionalmanager
                    applicants = Applicant.query.filter_by(regionalmanager=manager_name).all()
                    return render_template('dashboard.html', accounts=accounts, all_applicants=applicants,
                                           selected_menu='applicants')
            elif menu == 'account_managers':
                manager = regionalmanagermasterlist.query.filter(
                    regionalmanagermasterlist.manageremail.ilike(current_user.email)).first()
                print(manager.regionalmanager)
                if manager:
                    manager_name = manager.regionalmanager
                    account_managers = accountmanagermasterlist.query.filter_by(regionalmanager=manager_name).all()
                    return render_template('dashboard.html', accounts=accounts, account_managers=account_managers, selected_menu='account_managers')
    return render_template('login.html')


@dashboard.route('/get_employees/<job_name>/<job_number>')
def get_employees(job_name, job_number):
    global manager_name
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            # Get all the employees from employeemasterlist that have the specified job name
            employees = employeemasterlist.query.filter_by(jobname=job_name).all()

            # Get the jobs for the current manager
            jobs = get_manager_jobs(manager_name)
            accounts = get_user_accounts()

            return render_template('dashboard.html', employees=employees, jobs=jobs, accounts=accounts, job_name=job_name, selected_menu='employees')
        elif current_user.role == 'RegionalManager':
            # Get all the employees from employeemasterlist that have the specified job name
            employees = employeemasterlist.query.filter_by(jobname=job_name).all()

            accounts = get_user_accounts()

            return render_template('dashboard.html', employees=employees, accounts=accounts, job_name=job_name, selected_menu='employees')

@dashboard.route('/dashboard/open_positions')
def dashboard_open_positions():
    global manager_name
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            open_positions = get_open_positions(manager_name)
            jobs = get_manager_jobs(manager_name)
            accounts = get_user_accounts()
            return render_template('dashboard.html', open_positions=open_positions, jobs=jobs, accounts=accounts, selected_menu='open_positions')
        elif current_user.role == 'RegionalManager':
            accounts = get_user_accounts()
            open_positions = openpositionsroster.query.all()
            return render_template('dashboard.html', open_positions=open_positions, accounts=accounts, selected_menu='open_positions')
    return render_template('login.html')

@dashboard.route('/dashboard/open_positions/<job_name>')
def open_positions_by_job(job_name):
    global manager_name
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            open_positions = openpositionsroster.query.filter_by(accountmanager=manager_name, jobdescription=job_name).all()
            jobs = get_manager_jobs(manager_name)
            accounts = get_user_accounts()
            return render_template('dashboard.html', open_positions=open_positions, job_name=job_name, jobs=jobs, accounts=accounts, selected_menu='open_positions')
        elif current_user.role == 'RegionalManager':
            accounts = get_user_accounts()
            open_positions = openpositionsroster.query.filter_by(jobdescription=job_name).all()
            return render_template('dashboard.html', open_positions=open_positions, job_name=job_name, accounts=accounts, selected_menu='open_positions')
    return render_template('login.html')

@dashboard.route('/applicant/<applicantid>')
def view_applicant(applicantid):
    applicant = Applicant.query.filter_by(applicantid=applicantid).first()
    if applicant:
        return render_template('applicant.html', applicantid=applicantid, applicant=applicant)
    else:
        return render_template('error.html', message='Applicant not found')

@dashboard.route('/update_choice', methods=['POST'])
def update_choice():
    data = request.get_json()
    user_choice = data.get('choice')
    user_email = data.get('email')
    applicant_id = data.get('applicant_id')

    # Update the applicant's fields in the database
    applicant = Applicant.query.filter_by(applicantid=applicant_id).first()
    if applicant:
        current_time = datetime.now()

        # Update lastcontact field
        applicant.lastcontact = current_time

        # Update lastcontacttype field
        last_contact_type = f"{user_email}: {user_choice}"
        applicant.lastcontacttype = last_contact_type

        # Update contacthistory field
        if applicant.contacthistory:
            contact_history = eval(applicant.contacthistory)
        else:
            contact_history = {}

        contact_history[user_email] = {user_choice: current_time}
        applicant.contacthistory = str(contact_history)

        db.session.commit()

        # Update the HubSpot contact property
        hubspot_contact_id = applicant.hubspotcontactid
        print(hubspot_contact_id)
        if hubspot_contact_id:
            update_hubspot_contact_property(hubspot_contact_id, 'notes_last_contacted', current_time)
            # update_hubspot_contact_property(hubspot_contact_id, 'last_contact_type', last_contact_type)
            # update_hubspot_contact_property(hubspot_contact_id, 'contact_history', contact_history)

        return 'OK'

    return 'Applicant not found', 404