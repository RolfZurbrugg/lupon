from flask import request
from lupon import app

@app.route('/api/v1.0/contact', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_contact():
    
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
