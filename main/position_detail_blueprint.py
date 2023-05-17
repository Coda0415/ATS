from flask import Blueprint, render_template
from .models import openpositionsroster
from . import db

position_detail_blueprint = Blueprint('position_detail', __name__)

@position_detail_blueprint.route('/position/<position_id>')
def position_detail(position_id):
    # Get all positions from the openpositionsroster table with the same positionid prefix
    positions = db.session.query(openpositionsroster).filter(openpositionsroster.positionid.startswith(position_id)).all()

    # Select the first position from the list
    position = positions[0] if positions else None

    # Render the position.html template with the position details
    return render_template('position.html', position=position)
