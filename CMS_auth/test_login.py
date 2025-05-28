from app import app, db
from models import User
from check_password import check_login

test_credentials = [
    ("testuser", "password123"),
    ("student1", "student123")
]

print("Testing login credentials:")
for username, password in test_credentials:
    result = check_login(username, password)
    print(f"\nTesting login for {username}:")
    print(f"Password: {password}")
    print(f"Login successful: {result}") 