import sqlalchemy as sa
import sqlalchemy.orm as orm

from glittr.models.modelbase import SqlAlchemyBase

factory = None

def global_init(db_file: str):
    """
    Create connection to database
    """
    global factory
    
    if factory:
        return
    
    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    conn_str = 'sqlite:///' + db_file.strip()
    
    engine = sa.create_engine(conn_str, echo=True)
    factory = orm.sessionmaker(bind=engine)

    from glittr.models.db_models import Artist, Parent, Child, Instructor
    SqlAlchemyBase.metadata.create_all(engine)