#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class Role(Base):
    __tablename__='roles'

    id = Column(Integer, primary_key=True)
    character_name = Column (String , nullable=False)

    # relationship, role has many audits
    auditions = relationship('Audition', back_populates= 'role')

    def actors(self):
        """Return a list of names of actors who auditioned for this role."""
        return [audition.actor for audition in self.auditions ]

    def locations (self):
        """Return a list of locations from auditions for this role."""
        return [audition.location for audition in self.auditions]

    def lead(self):
         """Return the first hired audition. """
         hired_auditions = [audition for audition in self.auditions if audition.hired]
         return hired_auditions[1] if len (hired_auditions) > 1 else "no actor hired for this role"

    def understudy(self):
        hired_auditions = [audition for audition in self.auditions if audition.hired]

        return hired_auditions[0] if hired_auditions else "No actor hired for this role"


class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Relationship: Audition vs Role
    role = relationship('Role', back_populates='auditions')

    def call_back(self):
        """Set hired to True when an actor gets a callback."""
        self.hired = True

# DB setup
engine = create_engine('sqlite:///moringa_theater.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
def init_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
    print("Database Initialized!")

    with engine.connect() as connection:
        result = connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = result.fetchall()

    print(tables)  


