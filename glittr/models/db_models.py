import sqlalchemy as sa
from sqlalchemy.orm import relationship

from datetime import datetime

from glittr.models.modelbase import SqlAlchemyBase

class Artist(SqlAlchemyBase):
    __tablename__ = 'artists'

    artist_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    first_name = sa.Column(sa.String(15), nullable=False)
    last_name = sa.Column(sa.String(25), nullable=False)
    email = sa.Column(sa.String(100), unique=True, nullable=False)
    password_hash = sa.Column(sa.String(120), nullable=False)
    zip_code = sa.Column(sa.Integer, nullable=False)
    is_active = sa.Column(sa.Boolean, nullable=False)
    is_admin = sa.Column(sa.Boolean, nullable=False)
    inserted_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)

    # I don't really understand why we need this?
    # @classmethod
    # def from_dict(cls, artist_dict):
    #     result = cls(
    #         first_name=artist_dict["first_name"],
    #         last_name=artist_dict["last_name"],
    #         email=artist_dict["email"],
    #         password_hash=artist_dict["password_hash"],
    #         zip_code=artist_dict["zip_code"],
    #         is_active=artist_dict["is_active"],
    #         is_admin=artist_dict["is_admin"],
    #     )
    #     return result

    def __repr__(self):
        artist = {
            "artist_id": self.artist_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "zip_code": self.zip_code,
        }
        return json.dumps(artist)

class Parent(SqlAlchemyBase):
    __tablename__ = 'parents'

    parent_id = sa.Column(sa.Integer, primary_key=True)
    artist_id = sa.Column(sa.Integer, sa.ForeignKey("artists.artist_id"), nullable=False)
    inserted_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    children = relationship("Child")

    def __repr__(self):
        return f"Parent {self.parent_id}"


class Child(SqlAlchemyBase):
    __tablename__ = 'children'

    child_id = sa.Column(sa.Integer, primary_key=True)
    artist_id = sa.Column(sa.Integer, sa.ForeignKey("artists.artist_id"), nullable=False)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey("parents.parent_id"), nullable=False)
    date_of_birth = sa.Column(sa.DateTime, nullable=False)
    inserted_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"Child {self.child_id}"

class Instructor(SqlAlchemyBase):
    __tablename__ = 'instructors'

    instructor_id = sa.Column(sa.Integer, primary_key=True)
    artist_id = sa.Column(sa.Integer, sa.ForeignKey("artists.artist_id"), nullable=False)
    inserted_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    updated_dt = sa.Column(sa.DateTime, nullable=False, default=datetime.utcnow)
    def __repr__(self):
        return f"Instructor {self.instructor_id}"