import logging

from flask import g
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, login_user, current_user, logout_user

from lupon import app, db
from lupon.models import User
from lupon.forms import UserForm, LoginForm, UserProfileForm

@app.route('/register', methods=["GET", "POST"])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  
  form = UserForm()
  
  if form.validate_on_submit():

    try: 
        user = User()
        form.populate_obj(user)

        db.session.add(user)
        db.session.commit()
        flash("User successflly created!", 'success')
    
    except Exception as e:
        return e

    
    return redirect(url_for('index'))
  return render_template('register.html', form=form)

@app.route('/profile', methods=["GET", "POST"])
@login_required
def profile():
  form = UserProfileForm(obj=current_user)

  if form.validate_on_submit():
    form.populate_obj(current_user)
    db.session.commit()
    flash('Profile updated.', 'success')

  return render_template('profile.html', form=form)

def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    flash('not authenticated', 'danger')

    if form.validate_on_submit():
        flash('form is valide', 'info')
        user, authenticated = User.authenticate(form.email.data,
                                    form.password.data)

        if user and authenticated:
            remember = request.form.get('remember') == 'y'
            if login_user(user, remember=remember):
                flash("Logged in", 'success')
            return redirect(url_for('index'))
        else:
            flash('Sorry, invalid login', 'danger')

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out', 'success')
    return redirect(url_for('index'))