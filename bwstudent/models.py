from bwstudent import db


class Student(db.Model):
    __tablename__ = "student"
    english = db.Column(db.Float)
    python = db.Column(db.Float)
    c = db.Column(db.Float)
    sum = db.Column(db.Float)






