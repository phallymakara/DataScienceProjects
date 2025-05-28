from app import app, db
from models import User, Role

with app.app_context():
    # បង្កើតអ្នកប្រើប្រាស់សាកល្បង
    test_user = User(
        username='testuser',
        email='test@example.com',
        first_name='Test',
        last_name='User',
        role=Role.STUDENT
    )
    test_user.set_password('password123')
    
    # រក្សាទុកក្នុងមូលដ្ឋានទិន្នន័យ
    db.session.add(test_user)
    try:
        db.session.commit()
        print("Test user created successfully!")
        print(f"Username: {test_user.username}")
        print(f"Password: password123")
    except Exception as e:
        db.session.rollback()
        print(f"Error creating user: {str(e)}") 