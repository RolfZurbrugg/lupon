from flask import render_template
from flask_login import login_required
from lupon import app, db
from lupon.models import User


@app.route('/admin', methods=["GET", "POST"])
@login_required
def admin():
    users = User.query.all()
    return render_template('admin.html', users=users)