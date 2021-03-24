import sqlalchemy as sa
import sqlalchemy.orm as orm
from models.base import SqlAlchemyBase
from datetime import datetime

class Course(SqlAlchemyBase):

    __tablename__ = 'courses'

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255), nullable=False, index=True)
    summary = sa.Column(sa.Text)
    course_url = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)

    subject_id = sa.Column(sa.Integer, sa.ForeignKey('subjects.id'))
    subject = orm.relation('Subject')
