from datetime import datetime
from medical import db





class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), unique=True, nullable=False)
    lastname = db.Column(db.String(20), unique=True, nullable=False)
    jobname = db.Column(db.String(20), unique=True, nullable=False)
    hospital = db.Column(db.String(20), unique=True, nullable=False)
    rmdc = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    patients = db.relationship('Patient', backref='dr_names', lazy=True)
    

    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.jobname}', '{self.hospital}', '{self.rmdc}', '{self.email}')"


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patient_names = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    test = db.Column(db.String(100), nullable=False)
    result = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    medical_imaging = db.Column(db.String(20), nullable=False, default='default.jpg')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Patient('{self.patient_names}', '{self.date_posted}')"
