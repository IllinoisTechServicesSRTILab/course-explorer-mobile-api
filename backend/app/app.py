from flask import Flask
from flask_restx import Api
from .main.courseController import api as courseapi
from .main.datasource.database import initialize_db


app = Flask(__name__)

DB_URL = 'mongodb+srv://user1:rockwire@cluster0-wlgwx.mongodb.net/grade_db?retryWrites=true&w=majority'
app.config['MONGODB_HOST'] = DB_URL
initialize_db(app)

api = Api(app)
api.add_namespace(courseapi, path='/course')

app.run(host='0.0.0.0')
