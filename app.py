import uvicorn
from fastapi import FastAPI
import os
import glittr.models.db_session as db_session

app = FastAPI()

def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'glittr.db')

    db_session.global_init(db_file)

def main():
    setup_db()
    uvicorn.run(app)

if __name__ == '__main__':
    main()