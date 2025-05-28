from app import app, db
from models import User

def check_login(username, password):
    with app.app_context():
        user = User.query.filter_by(username=username).first()
        if user:
            print(f"Found user: {user.username}")
            if user.check_password(password):
                print("Password is correct!")
                return True
            else:
                print("Password is incorrect!")
                return False
        else:
            print(f"No user found with username: {username}")
            return False

# ព្យាយាមចូលប្រើប្រាស់ជាមួយ testuser
print("\nTesting login with testuser:")
check_login('morkmongkul', 'Monkhol123') 