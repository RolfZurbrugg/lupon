
def signup(self, parameter_list):
    pass

@app.route('/register', methods=["GET", "POST"])
def register():
  form = UserCreateForm()
  user = User.()
  if form.validate_on_submit():
    user = User(
                form.email.data, 
                form.username.data, 
                form.password.data
              )
    # db.session.add(user)
    user.update
    flash("User successflly created!")
    return redirect(url_for('register'))
  return render_template('register.html', form=form, users=users)
