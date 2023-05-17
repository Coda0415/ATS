from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user
from main.models import user
import bcrypt
import logging
from sqlalchemy import func

main = Blueprint('main', __name__)

logger = logging.getLogger(__name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email').lower()  # Convert email to lowercase
        password = request.form.get('password')

        # Find user by case-insensitive email comparison
        found_user = user.query.filter(func.lower(user.email) == email).first()

        if not found_user or not bcrypt.checkpw(password.encode('utf-8'), found_user.password.encode('utf-8')):
            flash('Invalid email or password', 'error')
            return redirect(url_for('main.index'))

        # Login user
        login_user(found_user)

        # Redirect to dashboard after login
        return redirect(url_for('dashboard.dashboard_view'))

    return render_template('login.html')



@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
