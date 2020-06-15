from .database import db
import uuid

class Term(db.EmbeddedDocument):
    term_name = db.StringField(required=True)
    A = db.IntField()
    B = db.IntField()
    C = db.IntField()
    D = db.IntField()
    F = db.IntField()


class Professor(db.EmbeddedDocument):
    professor_name = db.StringField(required=True)
    professor_avg = db.FloatField()
    terms = db.EmbeddedDocumentListField(Term)
    professor_students = db.IntField(default=0)


class Course(db.Document):
    course_id = db.StringField(required=True,unique=True)
    course_name = db.StringField(required=True)
    course_students = db.IntField(default=0)
    avg_gpa = db.FloatField(default=0.0)
    professors = db.EmbeddedDocumentListField(Professor)





