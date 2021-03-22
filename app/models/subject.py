import sqlalchemy as sa
from models.base import SqlAlchemyBase

class Subject(SqlAlchemyBase):

    __tablename__= 'subjects'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    description = sa.Column(sa.String)
    created_at = sa.Column(sa.DateTime)

    def __repr__(self):
        return f'< Subject {self.id}: {self.name} >'
    
