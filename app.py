#!flask/bin/python

from flask import Flask, jsonify, json
from bson import json_util
from flask_pymongo import PyMongo
from flask import request, abort
import ast

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "durkadurka"
mongo = PyMongo(app)


@app.route("/")
def index():
    return "MurkaDurka Service"


@app.route('/ddapi/v1.0/durkadurka', methods=['GET'])
def get_dds():
    ret = []
    for dd in mongo.db.dd.find({}, {'durka1' : 1, 'durka2': 1, '_id': 1}):
        print "DD: {}".format(dd)
        dd['_id'] = str(dd['_id'])
        ret.append(dd)

    return jsonify(ret)


#
# Create a new DurkaDurka by posting it.
#

@app.route('/ddapi/v1.0/durkadurka', methods=['POST'])
def create_dd():
    if not request.json or 'durka1' not in request.json or 'durka2' not in request.json:
        abort(400)

    durka1=request.json['durka1']
    durka2=request.json['durka2']

    mongo.db.dd.insert_one(request.json)

    return durka2



if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5001)

