from flask import Blueprint, render_template, request, redirect, url_for
import requests
from .models import applicants
from datetime import datetime
from . import db
from .functions import generate_applicant_id
import base64
import pickle


application_blueprint = Blueprint('application', __name__)

@application_blueprint.route('/application', methods=['GET', 'POST'])
def application():
    position_id = request.args.get('position_id')
    regional_manager = request.args.get('regional_manager')
    account_manager = request.args.get('account_manager')
    job_number = request.args.get('job_number')

    if request.method == 'POST':
        form_data = request.form.to_dict()
        portal_id = '9145139'
        form_guid = '15980c96-f3c1-41e8-a75d-96e0e50ff814'
        api_url = f'https://api.hsforms.com/submissions/v3/integration/submit/{portal_id}/{form_guid}'
        private_app_access_token = 'pat-na1-12bad899-4b41-48a4-b609-f6ea32f91a68'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {private_app_access_token}'
        }

        data = {
            'fields': [
                {
                    'objectTypeId': '0-1',
                    'name': 'address',
                    'value': form_data.get('address', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'preferred_name',
                    'value': form_data.get('preferred_name', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'are_you_at_least_18_years_old_',
                    'value': form_data.get('are_you_at_least_18_years_old_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'are_you_legally_eligible_to_work_in_the_us_',
                    'value': form_data.get('are_you_legally_eligible_to_work_in_the_us_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'are_you_looking_for_full_time_or_part_time_employment_',
                    'value': form_data.get('are_you_looking_for_full_time_or_part_time_employment_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'best_way_to_contact_you_',
                    'value': form_data.get('best_way_to_contact_you_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'city',
                    'value': form_data.get('city', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'company',
                    'value': form_data.get('company', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'content',
                    'value': form_data.get('content', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'start',
                    'value': form_data.get('start', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'date_available_to_start_work_',
                    'value': form_data.get('date_available_to_start_work_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'do_you_have_2_forms_of_identification__are_they_valid_and_are_they_hard_copies_',
                    'value': form_data.get(
                        'do_you_have_2_forms_of_identification__are_they_valid_and_are_they_hard_copies_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'email',
                    'value': form_data.get('email', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'end',
                    'value': form_data.get('end', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'firstname',
                    'value': form_data.get('firstname', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'have_you_ever_applied_or_been_employed_by_frantz_building_services_',
                    'value': form_data.get('have_you_ever_applied_or_been_employed_by_frantz_building_services_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'job_location',
                    'value': form_data.get('job_location', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'jobtitle',
                    'value': form_data.get('jobtitle', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'lastname',
                    'value': form_data.get('lastname', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'may_we_contact_this_employer_',
                    'value': form_data.get('may_we_contact_this_employer_', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'no_contact_explanation',
                    'value': form_data.get('no_contact_explanation', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'phone',
                    'value': form_data.get('phone', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'name_of_one_person_who_would_confirm_how_great_an_employee_you_are',
                    'value': form_data.get('name_of_one_person_who_would_confirm_how_great_an_employee_you_are', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'state',
                    'value': form_data.get('state', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'supervisor__phone_number',
                    'value': form_data.get('supervisor__phone_number', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'role_description',
                    'value': form_data.get('duties', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'supervisor_name',
                    'value': form_data.get('supervisor_name', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'reason_for_leaving_',
                    'value': form_data.get('reason_for_leaving', '')
                },
                {
                    'objectTypeId': '0-1',
                    'name': 'their_phone_number',
                    'value': form_data.get('their_phone_number', '')
                },

            ],
            'context': {
                'pageUri': request.url,
                'pageName': 'Application Form'
            }
        }
        response = requests.post(api_url, json=data, headers=headers)
        if response.status_code == 200:
            applicant_id = generate_applicant_id(position_id)

            form_dict = {item['name']: item['value'] for item in data['fields']}

            new_application = applicants(
                address=form_dict.get('address', ''),
                are_you_at_least_18_years_old_=form_dict.get('are_you_at_least_18_years_old_', ''),
                are_you_legally_eligible_to_work_in_the_us_=form_dict.get('are_you_legally_eligible_to_work_in_the_us_',
                                                                          ''),
                full_time_or_part_time_employment_=form_dict.get(
                    'are_you_looking_for_full_time_or_part_time_employment_', ''),
                best_way_to_contact_you_=form_dict.get('best_way_to_contact_you_', ''),
                city=form_dict.get('city', ''),
                company=form_dict.get('company', ''),
                content=form_dict.get('content', ''),
                startdate=datetime.strptime(form_dict.get('start', ''), "%Y-%m-%d") if form_dict.get('start',
                                                                                                     '') else None,
                date_available_to_start_work_=datetime.strptime(form_dict.get('date_available_to_start_work_', ''),
                                                                "%Y-%m-%d") if form_dict.get(
                    'date_available_to_start_work_', '') else None,
                two_forms_of_id_valid_and_hard_copies=form_dict.get(
                    'do_you_have_2_forms_of_identification__are_they_valid_and_are_they_hard_copies_', ''),
                email=form_dict.get('email', ''),
                enddate=datetime.strptime(form_dict.get('end', ''), "%Y-%m-%d") if form_dict.get('end', '') else None,
                firstname=form_dict.get('firstname', ''),
                applied_or_employed_by_frantz_building_services=form_dict.get(
                    'have_you_ever_applied_or_been_employed_by_frantz_building_services_', ''),
                job_location=form_dict.get('job_location', ''),
                jobtitle=form_dict.get('jobtitle', ''),
                lastname=form_dict.get('lastname', ''),
                may_we_contact_this_employer_=form_dict.get('may_we_contact_this_employer_', ''),
                no_contact_explanation=form_dict.get('no_contact_explanation', ''),
                phone=form_dict.get('phone', ''),
                one_person_who_would_confirm_great_employee=form_dict.get(
                    'name_of_one_person_who_would_confirm_how_great_an_employee_you_are', ''),
                state=form_dict.get('state', ''),
                supervisor__phone_number=form_dict.get('supervisor__phone_number', ''),
                role_description=form_dict.get('duties', ''),
                supervisor_name=form_dict.get('supervisor_name', ''),
                reason_for_leaving_=form_dict.get('reason_for_leaving', ''),
                their_phone_number=form_dict.get('their_phone_number', ''),
                applicantid=applicant_id,
                # applicantid will be positionid.number of applicants for that position.  For instance, if the positionid is 1148.pt.1.3 then the
                # applicantid will be 1148.pt.1.3.1 for the first applicant on that job, 1148.pt.1.3.2 for the second. etc...
                accountmanager= request.args.get('account_manager'),
                # account manager of the job applied for
                regionalmanager= request.args.get('regional_manager'),
                # regionalmanager of the job applied for
                eligibleforhire=None,
                # Yes - No
                applicantstatus="Applied",
                # Applied, interview-scheduled, pending background, interview scheduled, cold, no thanks.
                hubspotcontactid=None,
                # need to retrieve the id of the contact object in hubspot,
                contacthistory=None,
                # list of lists [[]Phonecall, datetime, notes],etc..]
                lastcontact=None,
                # datetime of last contact
                lastcontacttype=None,
                # type of last contact... with notes
                nextcontact=None,
                # date of next needed contact, either scheduled or based on template
                nextcontacttype=None,
                # type of next contact
                dateapplied=None,
                # date applicant applied for position
                backgroundcheck=None,
                # Passed, failed, pending, or null
                idstatus=None,
                # submitted, verified, waiting, or null
                drugscreen=None,
                # passed, failed, or null
                positionid = request.args.get('position_id'),
                jobnumber=request.args.get('job_number'),
                preferred_name=request.args.get('preferred_name')
            )

            db.session.add(new_application)
            db.session.commit()

            firstname = new_application.firstname
            lastname = new_application.lastname
            email = new_application.email
            applicant_id = new_application.applicantid

            return redirect(url_for('esign.esign', firstname=firstname, lastname=lastname, email=email,
                                    applicantid=applicant_id))
        else:
            return f'Error submitting form: {response.text}', 400

    return render_template('application.html', position_id=position_id, regional_manager=regional_manager,
                           account_manager=account_manager)
