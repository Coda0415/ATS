from flask import Blueprint, render_template
from flask_login import current_user
from .models import db, jobmasterlist, accountmanagermasterlist, employeemasterlist, openpositionsroster, applicants as Applicant

dashboard = Blueprint('dashboard', __name__, template_folder='templates')


def get_manager_jobs(manager_name):
    jobs = jobmasterlist.query.filter(jobmasterlist.accountmanager.contains(manager_name)).all()
    # print(f"Jobs for manager {manager_name}: {jobs}")
    return jobs


def get_open_positions(manager_name):
    open_positions = openpositionsroster.query.filter_by(accountmanager=manager_name).all()
    # print(f"Open positions for manager {manager_name}: {open_positions}")
    return open_positions


@dashboard.route('/dashboard', methods=['GET'])
def dashboard_view():
    if current_user.is_authenticated:
        if current_user.role == 'AccountManager':
            manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
            if manager:
                manager_name = manager.accountmanager
                jobs = get_manager_jobs(manager_name)
                open_positions = get_open_positions(manager_name)
                return render_template('dashboard.html', jobs=jobs, open_positions=open_positions)
    return render_template('login.html')



@dashboard.route('/open_positions')
def open_positions():
    manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
    if manager:
        manager_name = manager.accountmanager
        open_positions = get_open_positions(manager_name)
    return render_template('open_positions.html', open_positions=open_positions)


@dashboard.route('/get_employees/<job_name>/<job_number>')
def get_employees(job_name,job_number):
    # Get all the employees from employeemasterlist that have the specified job name
    employees = employeemasterlist.query.filter_by(jobname=job_name).all()

    # Get the jobs and open positions for the current manager
    manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
    if manager:
        manager_name = manager.accountmanager
        jobs = get_manager_jobs(manager_name)
        open_positions = get_open_positions(manager_name)

        # Retrieve applicants for the selected job
        applicants = Applicant.query.filter_by(jobnumber=job_number).all()


        return render_template('dashboard.html', employees=employees, open_positions=open_positions, jobs=jobs, job_name=job_name, applicants=applicants)




@dashboard.route('/dashboard/open_positions')
def dashboard_open_positions():
    if current_user.is_authenticated and current_user.role == 'AccountManager':
        manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
        if manager:
            manager_name = manager.accountmanager
            open_positions = openpositionsroster.query.filter_by(accountmanager=manager_name).all()
            return render_template('open_positions.html', open_positions=open_positions)
    return render_template('login.html')

@dashboard.route('/dashboard/open_positions/<job_name>')
def open_positions_by_job(job_name):
    if current_user.is_authenticated and current_user.role == 'AccountManager':
        manager = accountmanagermasterlist.query.filter_by(manageremail=current_user.email).first()
        if manager:
            manager_name = manager.accountmanager
            open_positions = openpositionsroster.query.filter_by(accountmanager=manager_name, jobdescription=job_name).all()
            jobs = get_manager_jobs(manager_name)  # Add this line to get jobs for the current manager
            return render_template('dashboard.html', open_positions=open_positions, job_name=job_name, jobs=jobs)
    return render_template('login.html')


