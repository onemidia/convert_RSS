from app.database import db

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    file_type = db.Column(db.String(10), nullable=False)  # txt ou csv
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())