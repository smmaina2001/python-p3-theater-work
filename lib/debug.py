#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from models import Base, engine, Role, Audition

# Initialize session
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if they don't exist
Base.metadata.create_all(engine)
print("Database created successfully!")

# Add roles
role1 = Role(character_name="SteveMwangi")
role2 = Role(character_name="David")
role2 = Role(character_name="Jane")


session.add_all([role1, role2])
session.commit()
print("Roles added successfully!")

# Add auditions
audition1 = Audition(actor="Will Smith", location="Los Angeles", phone="254722775430", hired=False, role=role1)
audition2 = Audition(actor="Don Johnson", location="Miami", phone="254722775431", hired=False, role=role2)
audition3 = Audition(actor="Kerry Washington", location="Florida", phone="254722775432", hired=False, role=role1)  # Fixed role

session.add_all([audition1, audition2, audition3])
session.commit()
print("Auditions added successfully !")

# Debugging mode
if __name__ == '__main__':
    import ipdb
    ipdb.set_trace()