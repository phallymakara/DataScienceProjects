from app import app, db
from models import User, Role
import logging

logging.basicConfig(level=logging.DEBUG)

def create_user(username, email, password, role=Role.STUDENT):
    with app.app_context():
        try:
            # ពិនិត្យមើលថាតើ username មានរួចហើយឬនៅ
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                print(f"Username {username} already exists!")
                return None

            # បង្កើតអ្នកប្រើប្រាស់ថ្មី
            user = User(
                username=username,
                email=email,
                role=role
            )
            user.set_password(password)
            
            # រក្សាទុកក្នុងមូលដ្ឋានទិន្នន័យ
            db.session.add(user)
            db.session.commit()
            
            print(f"User created successfully!")
            print(f"Username: {user.username}")
            print(f"Email: {user.email}")
            print(f"Role: {user.role}")
            
            # ព្យាយាមផ្ទៀងផ្ទាត់ពាក្យសម្ងាត់
            if user.check_password(password):
                print("Password verification successful!")
            else:
                print("Password verification failed!")
            
            return user
            
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            db.session.rollback()
            return None

# បង្កើតអ្នកប្រើប្រាស់ថ្មី
new_user = create_user(
    username="admin",
    email="admin@example.com",
    password="admin123",
    role=Role.ADMIN
) 