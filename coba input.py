from models import User, session  # Import the model and session

# Add new users
user1 = User(username="zarky", email="zarky@example.com")
user2 = User(username="zark", email="zark@example.com")

session.add(user1)
session.add(user2)
session.commit()

# Fetch users
users = session.query(User).all()
for user in users:
    print(user)

# Close session
session.close()
