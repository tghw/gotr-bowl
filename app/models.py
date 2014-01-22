from google.appengine.ext import db

class Score(db.Model):
    name = db.StringProperty(required=True)
    amount = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    updated = db.DateTimeProperty(auto_now=True)

    @property
    def formatted_amount(self):
        return '${:,.2f}'.format(self.amount / 100.0)

    @property
    def float_amount(self):
        return '{:.2f}'.format(self.amount / 100.0)
