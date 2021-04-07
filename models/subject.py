import sqlalchemy as sa
import sqlalchemy.orm as orm
from models.base import SqlAlchemyBase
from datetime import datetime

class Subject(SqlAlchemyBase):

    __tablename__= 'subjects'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=False)
    description = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow, index=True)
    updated_at = sa.Column(sa.DateTime, default=datetime.utcnow, index=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'))

    course = orm.relation('Course', cascade='all, delete', back_populates='subject')
    user = orm.relation('User')

    def __repr__(self):
        return f'< Subject {self.id}: {self.name} >'
    
