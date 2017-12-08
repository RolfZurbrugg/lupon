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


print(json.dumps(response.json(), indent=2))

r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=Winnetka&bounds=34.172684,-118.604794|34.236144,-118.500938&key=AIzaSyCuubDZxrnuw5KQPXrv0uleU32pFKye-7Y')

gmaps = googlemaps.Client(key='AIzaSyCuubDZxrnuw5KQPXrv0uleU32pFKye-7Y')
geocode_result = gmaps.geocode('Chutzenstrasse 1, Bremgarten bei Bern, Bern')
geocode_result[0]['geometry']['location']['lng']
geocode_result[0]['geometry']['location']['lat']