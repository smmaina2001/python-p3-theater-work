from config import engine, Base

if __name__ == "__main__":
    print("Running Migrations...")
    Base.metadata.create_all(engine)
    print("Migrations Done!")