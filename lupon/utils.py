'''
THIS MODULE IS STILL UNTESTED
putting some crypto toools in this utils class
'''
from .decorators import async
from sqlalchemy.ext.declarative import DeclarativeMeta
import
@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

'''
Source@ https://stackoverflow.com/questions/5022066/how-to-serialize-sqlalchemy-result-to-json
'''
def ():
    res = conn.execute(select([accounts]))

    # return all rows as a JSON array of objects
    return json.dumps([dict(r) for r in res])

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
            try:
                json.dumps(data) # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:
                fields[field] = None
                # a json-encodable dict
            return fields
            
            return json.JSONEncoder.default(self, obj)

