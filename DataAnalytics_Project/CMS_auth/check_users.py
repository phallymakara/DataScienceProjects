from app import app, db
from models import User

with app.app_context():
    users = User.query.all()
    print("Users in database:")
    for user in users:
        print(f"- Username: {user.username}")
        print(f"  Email: {user.email}")
        print(f"  Role: {user.role}")
        print("---") 