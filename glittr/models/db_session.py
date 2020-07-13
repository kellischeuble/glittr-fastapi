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

    #conn_str = 'sqlite:///' + db_file.strip()
    conn_str='sqlite:///:memory:'

    print(conn_str)
    
    engine = sa.create_engine(conn_str, echo=True, connect_args={"check_same_thread": False})
    factory = orm.sessionmaker(bind=engine)

    from glittr.models.db_models import Artist, Parent, Child, Instructor
    SqlAlchemyBase.metadata.create_all(engine)