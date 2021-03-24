import sqlalchemy as sa
import sqlalchemy.orm as orm
from models.base import SqlAlchemyBase

factory = None

def global_init(conn_string):
    global factory

    if factory:
        return

    if not conn_string or not conn_string.strip():
        raise Exception('Need db connection string')

    engine = sa.create_engine(conn_string, echo=True)
    factory = orm.sessionmaker(bind=engine)

    import models.__all_models
    SqlAlchemyBase.metadata.create_all(engine)
