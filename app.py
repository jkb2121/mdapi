#!flask/bin/python

from flask import Flask, jsonify, json
from bson import json_util
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "durkadurka"
mongo = PyMongo(app)


@app.route("/")
def index():
    ret = ""
    for dd in mongo.db.dd.find():
        ret += str(dd)
    return ret

    #json.dumps(ret, sort_keys=True, indent=4, default=json_util.default)


if __name__ == "__main__":
    app.run()
