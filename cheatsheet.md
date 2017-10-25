from lupon import app, db

app.app_context().push()
db.create_all()

<form action="{{ url_for('register') }}"  method="POST">
   <h2 class="form-signin-heading">Create new Account</h2>            
   {% for field in form %}
   <label class="{{ field.class }}" for="event_{{ field.id }}">{{ field.label }}</label>
   {{ field }}
   {% if form.errors %}
       <ul class="errors">{% for error in field.errors %}<li>{{ error }}</li>{% endfor %}</ul>
   {% endif %}
   {% endfor %}
   <p><input type="Submit" value="Register Now!"></p>
   {# form.csrf_token #}
</form>