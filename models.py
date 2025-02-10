from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the Base
Base = declarative_base()

# Create the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(100), unique=True)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

# Database Connection (change 'sqlite:///mydatabase.db' if needed)
engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)  # Create tables

# Create Session
Session = sessionmaker(bind=engine)
session = Session()
