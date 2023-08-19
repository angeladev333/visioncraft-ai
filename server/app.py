from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)



@app.route('/')
def index():
    data ={
        'Type':'Person',
        'Age':18
    }
    return data

if __name__ == '__main__':
    app.run(debug=True)