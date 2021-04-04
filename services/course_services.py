import db_session
from models.course import Course

def create_course(name, summary, course_url, subject):
    session = db_session.create_session()

    c = Course() 
    c.name = name
    c.summary = summary
    c.course_url = course_url
    c.subject_id = subject.id

    session.add(c)
    session.commit()

    return c

def get_course_by_id(course_id):
    session = db_session.create_session()
    course = session.query(Course).filter(Course.id == course_id).first()

    return course

def get_courses_by_subject(subject):
    session = db_session.create_session()
    courses = session.query(Course).filter(Course.subject_id == subject.id).all()

    return courses
  
