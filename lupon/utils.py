'''
THIS MODULE IS STILL UNTESTED
'''
from .decorators import async

@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)



def initDB():
    from lupon import app, db
    from lupon import models
    db.drop_all()
    db.create_all()
