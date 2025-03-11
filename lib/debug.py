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
role1 = Role(character_name="Scarzze")
role2 = Role(character_name="Omello")
role2 = Role(character_name="joy")


session.add_all([role1, role2])
session.commit()
print("Roles zimeongezwa!")

# Add auditions
audition1 = Audition(actor="Willy Paul", location="Racecourse", phone="254789034321", hired=False, role=role1)
audition2 = Audition(actor="Guy Fawkes", location="Theater", phone="254789034322", hired=False, role=role2)
audition3 = Audition(actor="Scar Mkadinali", location="Circle", phone="254789034323", hired=False, role=role1)  # Fixed role

session.add_all([audition1, audition2, audition3])
session.commit()
print("Auditions zimeongezwa!")

# Debugging mode
if __name__ == '__main__':
    import ipdb
    ipdb.set_trace()