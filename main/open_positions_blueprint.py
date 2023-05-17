from flask import Blueprint, render_template
from .models import openpositionsroster
from . import db

open_positions_blueprint = Blueprint('open_positions', __name__)

@open_positions_blueprint.route("/open_positions")
def open_positions():
    # Query the openpositionsroster table to get all open positions
    open_positions = db.session.query(openpositionsroster).all()

    # Create a dictionary to keep track of unique positionids
    unique_positions = {}

    # Loop through the open_positions and add unique positionids to the dictionary
    for position in open_positions:
        # Extract the positionid prefix (everything before the last period)
        position_id_prefix = ".".join(position.positionid.split(".")[:-1])

        # If the positionid prefix is not in the unique_positions dictionary, add it
        if position_id_prefix not in unique_positions:
            unique_positions[position_id_prefix] = position

    # Render a new template to display the open positions
    return render_template("open_positions.html", open_positions=unique_positions.values())
