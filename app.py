#!flask/bin/python

from flask import Flask, jsonify
from bson import ObjectId
from flask_pymongo import PyMongo
from flask import request, abort


app = Flask(__name__)
app.config["MONGO_DBNAME"] = "durkadurka"
mongo = PyMongo(app)


#
# Default route
#
@app.route("/")
def index():
    return "MurkaDurka API"


#
# Return all DurkaDurkas in the system
#
@app.route('/ddapi/v1.0/durkadurka', methods=['GET'])
def get_dds():
    ret = []
    for dd in mongo.db.dd.find({}, {'durka1': 1, 'durka2': 1, '_id': 1}):
        print "DD: {}".format(dd)
        dd['_id'] = str(dd['_id'])
        ret.append(dd)

    return jsonify(ret)


#
# Return a specific DurkaDurka given an id.
#
@app.route('/ddapi/v1.0/durkadurka/<string:dd_id>', methods=['GET'])
def get_one_dd(dd_id):
    ret = []
    for dd in mongo.db.dd.find({'_id': ObjectId(dd_id)}, {'durka1': 1, 'durka2': 1, '_id': 1}):
        print "DD: {}".format(dd)
        dd['_id'] = str(dd['_id'])
        ret.append(dd)

    return jsonify(ret)


#
# Route and Function to delete the DurkaDurka given a DurkaDurka id.
#
@app.route('/ddapi/v1.0/durkadurka/<string:dd_id>', methods=['DELETE'])
def delete_dd(dd_id):
    try:
        mongo.db.dd.remove({'_id': ObjectId(dd_id)})
        return jsonify({'result': True})
    except:
        return jsonify({'result': False})


#
# Route and Function to Update the DurkaDurka specified by the id
#
@app.route('/ddapi/v1.0/durkadurka/<string:dd_id>', methods=['PUT'])
def update_dd(dd_id):
    if not request.json or 'durka1' not in request.json or 'durka2' not in request.json:
        abort(400)

    try:
        mongo.db.dd.update_one(
            {'_id': ObjectId(dd_id)},
            {
                '$set': {
                    "durka1": request.json['durka1'],
                    "durka2": request.json['durka2']
                }
            }
        )
        return jsonify({'result': True})
    except:
        return jsonify({'result': False})


#
# Create a new DurkaDurka by posting it.
#
@app.route('/ddapi/v1.0/durkadurka', methods=['POST'])
def create_dd():
    if not request.json or 'durka1' not in request.json or 'durka2' not in request.json:
        abort(400)

    # Probably want some error checking to make sure what we pass in is OK
    # durka1 = request.json['durka1']
    # durka2 = request.json['durka2']

    try:
        mongo.db.dd.insert_one(request.json)
        return jsonify({'result': True})
    except:
        return jsonify({'result': False})




if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=5001)

