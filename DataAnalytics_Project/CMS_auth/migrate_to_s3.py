import os
from app import app, db
from models import User, Course
from s3_utils import S3Handler
from flask import current_app

def migrate_profile_images():
    """Migrate user profile images to S3"""
    with app.app_context():
        s3 = S3Handler()
        users = User.query.filter(User.profile_image_url.isnot(None)).all()
        
        for user in users:
            if user.profile_image_url and not user.profile_image_url.startswith('https://'):
                try:
                    # Get local file path
                    local_path = os.path.join(app.config['UPLOAD_FOLDER'], 'profiles', 
                                            os.path.basename(user.profile_image_url))
                    
                    if os.path.exists(local_path):
                        # Upload to S3
                        with open(local_path, 'rb') as file:
                            s3_url = s3.upload_file(file, folder='profiles')
                            if s3_url:
                                user.profile_image_url = s3_url
                                db.session.commit()
                                print(f"Migrated profile image for user {user.username}")
                            else:
                                print(f"Failed to upload profile image for user {user.username}")
                except Exception as e:
                    print(f"Error migrating profile image for user {user.username}: {str(e)}")

def migrate_course_thumbnails():
    """Migrate course thumbnails to S3"""
    with app.app_context():
        s3 = S3Handler()
        courses = Course.query.filter(Course.thumbnail_url.isnot(None)).all()
        
        for course in courses:
            if course.thumbnail_url and not course.thumbnail_url.startswith('https://'):
                try:
                    # Get local file path
                    local_path = os.path.join(app.config['UPLOAD_FOLDER'], 'thumbnails', 
                                            os.path.basename(course.thumbnail_url))
                    
                    if os.path.exists(local_path):
                        # Upload to S3
                        with open(local_path, 'rb') as file:
                            s3_url = s3.upload_file(file, folder='thumbnails')
                            if s3_url:
                                course.thumbnail_url = s3_url
                                db.session.commit()
                                print(f"Migrated thumbnail for course {course.title}")
                            else:
                                print(f"Failed to upload thumbnail for course {course.title}")
                except Exception as e:
                    print(f"Error migrating thumbnail for course {course.title}: {str(e)}")

if __name__ == '__main__':
    print("Starting migration to S3...")
    migrate_profile_images()
    migrate_course_thumbnails()
    print("Migration completed!") 