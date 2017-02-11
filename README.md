# mdapi
MongaDurka API

------
The MongaDurka API tests a create, read, update and delete API but putting the data into a MongoDB. 

Next:
 * We need to somehow use flask-mongoengine, a convenient ORM for MongoDB  http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
 * HADEOS
 * Error checking on input
 * returning a 404 at the right time?
 * ...and Unit Tests!!




---------

Notes:
 * Don't forget to configure pycharm to work with our virtualenv!   http://exponential.io/blog/2015/02/10/configure-pycharm-to-use-virtualenv/
 * Added flask_pymongo (for Flask), pymongo for the standalone
 * How do I .gitignore the .idea/ and flask/ directories? 