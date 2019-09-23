from datetime import datetime

from ..app import db


class TimeStampedModel(db.Model):
    __abstract__ = True

    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.modified_at = datetime.utcnow()
