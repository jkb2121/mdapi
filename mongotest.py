#!flask/bin/python

from pymongo import MongoClient

client = MongoClient()
db = client.durkadurka

result = db.dd.insert_one(
    {
        "durka1": "monga2",
        "durka2": "durka2"
    }
)

print "Inserted: {}".format(result.inserted_id)

