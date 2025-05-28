from app import app, db
from models import User, Role

def create_test_user():
    with app.app_context():
        # Check if user already exists
        if User.query.filter_by(username='testuser').first():
            print('User testuser already exists')
            return
        
        # Create new user
        user = User(
            username='testuser',
            email='test@example.com',
            first_name='Test',
            last_name='User',
            role=Role.STUDENT
        )
        user.set_password('password123')
        
        # Add to database
        db.session.add(user)
        db.session.commit()
        print('Created user testuser')

if __name__ == '__main__':
    create_test_user() 