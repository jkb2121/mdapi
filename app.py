#!flask/bin/python

from flask import Flask, jsonify
from bson import ObjectId, json_util
# from flask_pymongo import PyMongo
from flask import request, abort
from flask_mongoengine import MongoEngine, Document, DynamicDocument
from mongoengine.fields import StringField

app = Flask(__name__)
#app.config["MONGO_DBNAME"] = "durkadurka"
# mongo = PyMongo(app)
app.config['MONGODB_SETTINGS'] = {
    'db': 'durkadurka'
}
mongo = MongoEngine(app)
mongo.connect()


class DurkaDurka(DynamicDocument):
    meta = {
        'collection': 'dd'
    }
    _id = StringField
    durka1 = StringField()
    durka2 = StringField()

    def display(self):
        print "ID: {}, DD1: {}, DD2: {}".format(self._id, self.durka1, self.durka2)

    def setDurka1(self, durka1):
        self.durka1 = durka1
        self.save()

    def setDurka2(self, durka2):
        self.durka2 = durka2
        self.save()


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
    # ret = []
    # for dd in mongo.dd.find({}, {'durka1': 1, 'durka2': 1, '_id': 1}):
    #     print "DD: {}".format(dd)
    #     dd['_id'] = str(dd['_id'])
    #     ret.append(dd)
    #
    # return jsonify(ret)

    dd = DurkaDurka.objects()
    for d in dd:
        #print "ID: {}, DD1: {}, DD2: {}".format(d._id, d.durka1, d.durka2)
        d.display()

    # return json_util.dumps(dd._collection_obj.find(dd._query))
    return jsonify(dd)

#
# Return a specific DurkaDurka given an id.
#
@app.route('/ddapi/v1.0/durkadurka/<string:dd_id>', methods=['GET'])
def get_one_dd(dd_id):
    # ret = []
    # for dd in mongo.db.dd.find({'_id': ObjectId(dd_id)}, {'durka1': 1, 'durka2': 1, '_id': 1}):
    #     print "DD: {}".format(dd)
    #     dd['_id'] = str(dd['_id'])
    #     ret.append(dd)
    #
    # return jsonify(ret)
    d = DurkaDurka.objects.get(_id=ObjectId(dd_id))
    #for d in dd:
    #print "ID: {}, DD1: {}, DD2: {}".format(d._id, d.durka1, d.durka2)
    d.display()
    return jsonify(d)

#
# Route and Function to delete the DurkaDurka given a DurkaDurka id.
#
@app.route('/ddapi/v1.0/durkadurka/<string:dd_id>', methods=['DELETE'])
def delete_dd(dd_id):
    try:
        # mongo.db.dd.remove({'_id': ObjectId(dd_id)})
        DurkaDurka.objects(_id=ObjectId(dd_id)).delete()
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
        d = DurkaDurka.objects.get(_id=ObjectId(dd_id))
        # mongo.db.dd.update_one(
        #     {'_id': ObjectId(dd_id)},
        #     {
        #         '$set': {
        #             "durka1": request.json['durka1'],
        #             "durka2": request.json['durka2']
        #         }
        #     }
        # )

        d._id = dd_id
        d.durka1 = request.json['durka1']
        d.durka2 = request.json['durka2']
        d.save()

        # d.setDurka1(request.json['durka1'])
        # d.setDurka2(request.json['durka2'])

        return jsonify({'result': True})

    except Exception as e:
        print str(e)
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

