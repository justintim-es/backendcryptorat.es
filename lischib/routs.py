from lischib import app
from flask import request

@app.route('/register')
def register():
    json = request.json
