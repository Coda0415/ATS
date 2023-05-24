from flask import Blueprint, render_template
from flask_login import current_user
from .models import jobmasterlist, accountmanagermasterlist, employeemasterlist, openpositionsroster, applicants as Applicant

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

manager_name = None

def get_manager_jobs(manager_name):
    jobs = jobmasterlist.query.filter(jobmasterlist.accountmanager.contains(manager_name)).all()
    return jobs

def get_open_positions(manager_name):
    open_positions = openpositionsroster.query.filter_by(accountmanager=manager_name).all()
    return open_positions

def get_user_accounts():
    if current_user.is_authenticated and current_user.role == 'AccountManager':
        manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
        if manager:
            return jobmasterlist.query.filter(jobmasterlist.accountmanager.contains(manager.accountmanager)).all()
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
    return render_template('login.html')

@dashboard.route('/dashboard/<menu>', methods=['GET'])
def dashboard_view_menu(menu):
    global manager_name
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
            if manager:
                manager_name = manager.accountmanager
                jobs = get_manager_jobs(manager_name)
                accounts = get_user_accounts()
                if menu == 'employees':
                    return render_template('dashboard.html', jobs=jobs, accounts=accounts, selected_menu='employees')
                elif menu == 'open_positions':
                    open_positions = get_open_positions(manager_name)
                    return render_template('dashboard.html', jobs=jobs, accounts=accounts, open_positions=open_positions, selected_menu='open_positions')
                elif menu == 'applicants':
                    applicants = Applicant.query.filter_by().all()
                    return render_template('dashboard.html', jobs=jobs, accounts=accounts, all_applicants=applicants, selected_menu='applicants')
    return render_template('login.html')

@dashboard.route('/get_employees/<job_name>/<job_number>')
def get_employees(job_name, job_number):
    global manager_name
    # Get all the employees from employeemasterlist that have the specified job name
    employees = employeemasterlist.query.filter_by(jobname=job_name).all()

    # Get the jobs for the current manager
    jobs = get_manager_jobs(manager_name)
    accounts = get_user_accounts()

    return render_template('dashboard.html', employees=employees, jobs=jobs, accounts=accounts, job_name=job_name, selected_menu='employees')

@dashboard.route('/dashboard/open_positions')
def dashboard_open_positions():
    global manager_name
    if current_user.is_authenticated and current_user.role == 'AccountManager':
        open_positions = get_open_positions(manager_name)
        jobs = get_manager_jobs(manager_name)
        accounts = get_user_accounts()
        return render_template('dashboard.html', open_positions=open_positions, jobs=jobs, accounts=accounts, selected_menu='open_positions')
    return render_template('login.html')

@dashboard.route('/dashboard/open_positions/<job_name>')
def open_positions_by_job(job_name):
    global manager_name
    if current_user.is_authenticated and current_user.role == 'AccountManager':
        open_positions = openpositionsroster.query.filter_by(accountmanager=manager_name, jobdescription=job_name).all()
        jobs = get_manager_jobs(manager_name)
        accounts = get_user_accounts()
        return render_template('dashboard.html', open_positions=open_positions, job_name=job_name, jobs=jobs, accounts=accounts, selected_menu='open_positions')
    return render_template('login.html')
