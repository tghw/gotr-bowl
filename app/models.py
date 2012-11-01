from google.appengine.ext import db

class TestModel(db.Model):
    name = db.StringProperty(required=True)
    user = db.UserProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)
