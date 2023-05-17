from .models import applicants
from . import db

def generate_applicant_id(position_id):
    # Count the number of existing applicants for the position
    num_applicants = applicants.query.filter_by(positionid=position_id).count()

    # Create the applicantid using the positionid and the number of applicants
    applicant_id = f"{position_id}.{num_applicants + 1}"
    return applicant_id
