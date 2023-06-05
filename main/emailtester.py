from flask import Blueprint, render_template, request, redirect, url_for
from email.message import EmailMessage
import ssl
import smtplib
import requests

email_blueprint = Blueprint('email', __name__)

# Endpoint for the eligibility check form submission
@email_blueprint.route('/eligibility-check', methods=['POST'])
def eligibility_check():
    button_value = request.form.get('button')

    if button_value == 'yes':
        # Handle the "Yes" button logic
        print('You clicked "Yes"')
        return 'You clicked "Yes"'
    elif button_value == 'no':
        # Handle the "No" button logic
        print('You clicked "No"')
        return 'You clicked "No"'

    print('Invalid form submission')
    return 'Invalid form submission'


def send_email_with_info(form_dict, applicant_id, account_manager, regional_manager):
    email_sender = 'coda.frantz@gmail.com'
    email_password = 'hvuupecsdxjzvbkn'
    email_receiver = 'dojadox699@rockdian.com'
    others = 'cdavis@frantzbuilding.com'
    subject = 'Test Applicant'

    ngrok_url = 'https://87b9-216-135-51-150.ngrok-free.app'  # Replace with your ngrok URL

    # Construct the HTML body
    body = """
    <html>
    <head></head>
    <body>
        <h2>Job Application Information</h2>
        <p><strong>First Name:</strong> {first_name}</p>
        <p><strong>Last Name:</strong> {last_name}</p>
        <p><strong>Address:</strong> {address}</p>
        <p><strong>Are you at least 18 years old?:</strong> {age}</p>
        <p><strong>Legally eligible to work in the US?:</strong> {eligibility}</p>
        <p><strong>Full-time or Part-time employment?:</strong> {employment}</p>
        <p><strong>Best way to contact you:</strong> {contact}</p>
        <p><strong>City:</strong> {city}</p>
        <p><strong>Company:</strong> {company}</p>
        <p><strong>Content:</strong> {content}</p>
        <p><strong>Start Date:</strong> {start_date}</p>
        <p><strong>Date available to start work:</strong> {available_date}</p>
        <p><strong>Two forms of ID valid and hard copies:</strong> {id_valid}</p>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>End Date:</strong> {end_date}</p>
        <p><strong>Applied or Employed by Frantz Building Services:</strong> {applied_employed}</p>
        <p><strong>Job Location:</strong> {job_location}</p>
        <p><strong>Job Title:</strong> {job_title}</p>
        <p><strong>May we contact this employer:</strong> {may_contact}</p>
        <p><strong>No contact explanation:</strong> {no_contact_explanation}</p>
        <p><strong>Phone:</strong> {phone}</p>
        <p><strong>Name of person who would confirm your greatness as an employee:</strong> {confirm_name}</p>
        <p><strong>State:</strong> {state}</p>
        <p><strong>Supervisor's Phone Number:</strong> {supervisor_phone}</p>
        <p><strong>Role Description:</strong> {role_description}</p>
        <p><strong>Supervisor's Name:</strong> {supervisor_name}</p>
        <p><strong>Reason for Leaving:</strong> {reason_for_leaving}</p>
        <p><strong>Their Phone Number:</strong> {their_phone}</p>
        <p><strong>Applicant ID:</strong> {applicant_id}</p>
        <p><strong>Account Manager:</strong> {account_manager}</p>
        <p>
            <form method="post" action="{ngrok_url}/eligibility-check">
                <input type="hidden" name="button" value="yes">
                <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer;">
                    Yes
                </button>
            </form>
            <form method="post" action="{ngrok_url}/eligibility-check">
                <input type="hidden" name="button" value="no">
                <button type="submit" style="background-color: #f44336; color: white; padding: 10px 20px; border: none; cursor: pointer;">
                    No
                </button>
            </form>
        </p>
    </body>
    </html>
    """.format(
        address=form_dict.get('address', ''),
        age=form_dict.get('are_you_at_least_18_years_old_', ''),
        eligibility=form_dict.get('are_you_legally_eligible_to_work_in_the_us_', ''),
        employment=form_dict.get('are_you_looking_for_full_time_or_part_time_employment_', ''),
        contact=form_dict.get('best_way_to_contact_you_', ''),
        city=form_dict.get('city', ''),
        company=form_dict.get('company', ''),
        content=form_dict.get('content', ''),
        start_date=form_dict.get('start', ''),
        available_date=form_dict.get('date_available_to_start_work_', ''),
        id_valid=form_dict.get('do_you_have_2_forms_of_identification__are_they_valid_and_are_they_hard_copies_', ''),
        email=form_dict.get('email', ''),
        end_date=form_dict.get('end', ''),
        first_name=form_dict.get('firstname', ''),
        applied_employed=form_dict.get('have_you_ever_applied_or_been_employed_by_frantz_building_services_', ''),
        job_location=form_dict.get('job_location', ''),
        job_title=form_dict.get('jobtitle', ''),
        last_name=form_dict.get('lastname', ''),
        may_contact=form_dict.get('may_we_contact_this_employer_', ''),
        no_contact_explanation=form_dict.get('no_contact_explanation', ''),
        phone=form_dict.get('phone', ''),
        confirm_name=form_dict.get('name_of_one_person_who_would_confirm_how_great_an_employee_you_are', ''),
        state=form_dict.get('state', ''),
        supervisor_phone=form_dict.get('supervisor__phone_number', ''),
        role_description=form_dict.get('duties', ''),
        supervisor_name=form_dict.get('supervisor_name', ''),
        reason_for_leaving=form_dict.get('reason_for_leaving', ''),
        their_phone=form_dict.get('their_phone_number', ''),
        applicant_id=applicant_id,
        account_manager=request.args.get('account_manager'),
        regional_manager=request.args.get('regional_manager'),
        ngrok_url=ngrok_url
    )

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['CC'] = others
    em['Subject'] = subject
    em.add_alternative(body, subtype='html')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        recipients = [email_receiver] + others.split(', ')
        smtp.sendmail(email_sender, recipients, em.as_string())
