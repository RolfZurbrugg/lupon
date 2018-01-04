from lupon import api
from flask_restful import Resource

class ContactList(Resource):
    def get(self, id):
        return {'task': 'Say "Hello, World!"'}


api.add_resource(ContactList, '/api/v1.0/contact', endpoint='contact')