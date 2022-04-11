from datetime import datetime
from utils.db import db

class TimeModel(object):
    created_at = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    last_updated = db.Column(
        db.DateTime,default=datetime.utcnow , onupdate=datetime.utcnow
    )