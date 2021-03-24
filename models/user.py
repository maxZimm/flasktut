import sqlalchemy as sa
import sqlalchemy.orm as orm
from models.base import SqlAlchemyBase
from datetime import datetime

class User(SqlAlchemyBase):

    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String, nullable=True)
    last_name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True, nullable=True, index=True)
    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    created_at = sa.Column(sa.DateTime, default=datetime.utcnow)
    last_login = sa.Column(sa.DateTime, default=datetime.utcnow, index=True)

    subjects = orm.relation('Subject', back_populates='user')
