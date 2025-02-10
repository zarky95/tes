from database import User

# Connect to the database
engine = create_engine('sqlite:///mydatabase.db')  # Change to your DB connection
session = sessionmaker(bind=engine)
session = session()  # Create session

# Add data to the table
user1 = User(username="doe", email="doe@example.com")
user2 = User(username="smith", email="smith@example.com")

session.add(user1)
session.add(user2)
session.commit()  # Save changes

# Close session
session.close()
