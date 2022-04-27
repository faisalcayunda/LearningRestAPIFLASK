#import library
from urllib import response
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Initialized object
app = Flask(__name__)

# intialize object flask_resful
api = Api(app)

# initialize object flask cors

CORS(app)
# creating dictionary
identitas = {}

# creating class resource


class AppResource(Resource):
    # Creating method get and post
    # getting data
    def get(self):
        # response = {"msg": "Hello World, ini app restful pertama "}
        return identitas
    # postdata

    def post(self):
        nama = request.form["nama"]
        umur = request.form['umur']
        identitas['nama'] = nama
        identitas['umur'] = umur
        response = {"msg": "Data berhasil dimasukan"}
        return response


# setup resource
api.add_resource(AppResource, "/api", methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True, port=4321)
