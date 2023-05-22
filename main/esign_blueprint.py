from flask import Blueprint, render_template, request
from .models import applicants
from . import db

esign_blueprint = Blueprint('esign', __name__)


@esign_blueprint.route('/esign', methods=['GET', 'POST'])
def esign():
    position_id = request.args.get('position_id')
    regional_manager = request.args.get('regional_manager')
    account_manager = request.args.get('account_manager')
    job_number = request.args.get('job_number')

    if request.method == 'POST':
        form_data = request.form.to_dict()
        # Process the form data and handle the submission

        # Example: Access the values
        i_acknowledge = form_data.get('i_acknowledge_receipt_and_understanding_of_the_above')
        signature = form_data.get('applicant_signature')
        date_acknowledgement = form_data.get('date_of_electronic_acknowledgement')

        # Find the applicant in the database
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        email = request.args.get('email')
        applicant_id = request.args.get('applicantid')

        applicant = applicants.query.filter_by(firstname=firstname, lastname=lastname, email=email,
                                               applicantid=applicant_id).first()

        if applicant:
            # Update the applicant's information
            applicant.applicant_statement_acknowledgement = i_acknowledge
            applicant.applicant_statement_signature = signature
            applicant.applicant_statement_date_acknowledgement = date_acknowledgement

            db.session.commit()
            return 'Form submitted successfully'
        else:
            return 'Applicant not found in the database', 404

    return render_template('esign.html', position_id=position_id, regional_manager=regional_manager,
                           account_manager=account_manager, job_number=job_number)
