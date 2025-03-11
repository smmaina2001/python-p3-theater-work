from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config import Base, session, engine  # Import engine

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    character_name = Column(String, nullable=False, unique=True)

    # Relationship (one-to-many)
    auditions = relationship('Audition', back_populates='role')

    def actors(self):
        return [audition.actor for audition in self.auditions]

    def locations(self):
        return [audition.location for audition in self.auditions]

    def lead(self):
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[0] if hired_auditions else "No actor has been hired for this role"

    def understudy(self):
        hired_auditions = [a for a in self.auditions if a.hired]
        return hired_auditions[1] if len(hired_auditions) > 1 else "No actor has been hired for understudy for this role"

class Audition(Base):
    __tablename__ = 'auditions'

    id = Column(Integer, primary_key=True)
    actor = Column(String, nullable=False)
    location = Column(String, nullable=False)
    phone = Column(Integer, nullable=False)
    hired = Column(Boolean, default=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Relationship (many-to-one)
    role = relationship('Role', back_populates='auditions')

    def call_back(self):
        self.hired = True
        session.commit()  # Save change to database

# Create tables after defining models
Base.metadata.create_all(engine)