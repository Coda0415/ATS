from flask import Blueprint, request, flash, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime

from . import db
from .models import openpositionsroster, jobmasterlist

job_request_submission = Blueprint('job_request_submission', __name__)

def convert_to_12_hour_format(time24):
    time_object = datetime.strptime(time24, "%H:%M")
    formatted_time = time_object.strftime("%I:%M%p")
    formatted_time = formatted_time.replace("AM", "a").replace("PM", "p")

    if formatted_time.startswith("0"):
        formatted_time = formatted_time[1:]

    return formatted_time


def find_missing_days(day_input):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    days_dict = dict(zip(days, range(1, 8)))

    days_short = [day[:3] for day in day_input if (day_short := day.strip()[:3]) in days]

    day_numbers = sorted([days_dict[day] for day in days_short])

    working_days = [day_numbers[0]]
    is_consecutive = [True]

    for i in range(1, len(day_numbers)):
        diff = (day_numbers[i] - day_numbers[i - 1]) % 7
        if diff == 1:
            working_days.append(day_numbers[i])
            is_consecutive.append(True)
        else:
            working_days.append(day_numbers[i])
            is_consecutive.append(False)

    formatted_days = [days[working_days[0] - 1]]

    for i in range(1, len(working_days)):
        if is_consecutive[i]:
            if i == len(working_days) - 1 or not is_consecutive[i + 1]:
                formatted_days.append(f"-{days[working_days[i] - 1]}")
            continue
        else:
            formatted_days.append(f",{days[working_days[i] - 1]}")

    return "".join(formatted_days)

def create_open_position_ids(job_number, employment_type, shift_start_time, num_positions):
    employment_type_short = "FT" if employment_type == "Full-Time" else "PT"

    # Determine the shift number based on the shift_start_time
    shift_number = 0
    if 6 <= shift_start_time.hour < 14:
        shift_number = 1
        shift_name = '1st'
    elif 14 <= shift_start_time.hour < 22:
        shift_number = 2
        shift_name = '2nd'
    elif 22 <= shift_start_time.hour or shift_start_time.hour < 6:
        shift_number = 3
        shift_name = '3rd'

    open_position_ids = []
    for position_index in range(1, num_positions + 1):
        open_position_id = f"{job_number}.{employment_type_short}.{shift_number}.{position_index}"
        open_position_ids.append(open_position_id)

    return open_position_ids, employment_type_short, shift_name

# def shift_number_to_name(shift_number):
#     if shift_number == 1:
#         return "1st"
#     elif shift_number == 2:
#         return "2nd"
#     elif shift_number == 3:
#         return "3rd"
#     else:
#         return "Other"




@login_required
@job_request_submission.route("/JobRequestSubmission", methods=["POST"])
def submit_job_request():
    form_data = request.form
    starting_time_24 = form_data.get("starting-time")
    ending_time_24 = form_data.get("ending-time")

    starting_time_12 = convert_to_12_hour_format(starting_time_24)
    ending_time_12 = convert_to_12_hour_format(ending_time_24)
    workdays_input = request.form.getlist("workdays[]")
    workdays_range = find_missing_days(workdays_input)

    # Convert the start time to a datetime object
    shift_start_time = datetime.strptime(starting_time_24, "%H:%M")

    # Get the number of positions from the form data
    num_positions = int(form_data.get("num_positions", 1))

    # Convert the start time to a datetime object
    shift_start_time = datetime.strptime(starting_time_24, "%H:%M")

    # Create the PositionIDs and get the abbreviated employment type
    position_ids, employment_type_short, shift_name = create_open_position_ids(
        form_data.get('job_number'), form_data.get('employment_type'), shift_start_time, num_positions
    )

    # # Get the shift name based on the shift number
    # shift_name = shift_number_to_name(shift_number)

    # Retrieve data from JobsMasterList
    job_number = form_data.get("job_number")
    job_data = jobmasterlist.query.filter_by(jobnumber=job_number).first()
    print(form_data)
    for attr, value in job_data.__dict__.items():
        print(f"{attr}: {type(value)}")

    print()
    # Loop through the PositionIDs and insert each one into the database
    for position_id in position_ids:
        existing_position = openpositionsroster.query.filter_by(positionid=position_id).first()

        if existing_position is None:
            new_open_position = openpositionsroster(
                positionid=position_id,
                jobnumber=form_data.get('job_number'),
                jobtitle=form_data.get('job_title'),
                employmenttype=employment_type_short,
                wage=form_data.get('hourly-pay'),
                businesssegment=job_data.businesssegment,
                jobcity=job_data.jobcity,
                jobdescription=job_data.jobname,
                jobzip = job_data.jobzip.replace("-", ""),
                region=job_data.region,
                accountmanager=job_data.accountmanager,
                regionalmanager=job_data.regionalmanager,
                shift=shift_name,
                specialinstructions=','.join(request.form.getlist("special-instructions[]")),
                workdays=workdays_range,
                starttime=starting_time_12,
                endtime=ending_time_12,
                flextime=form_data.get('flex-hours'),
                sobamount=form_data.get('sobAmount'),
                sobdays=form_data.get('sobDays')
        )
            db.session.add(new_open_position)
        else:
            print(f"Position with PositionID {position_id} already exists. Skipping insertion.")

    # Commit the changes to the database
    db.session.commit()

    # Print a message to indicate successful insertion
    print(f"Inserted new positions: {position_ids}")

    # Redirect back to the JobRequestPage after submission
    return redirect(url_for("job_request_page.job_request_form"))
