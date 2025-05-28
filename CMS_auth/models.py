from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

# User roles
class Role:
    ADMIN = 'admin'
    INSTRUCTOR = 'instructor'
    STUDENT = 'student'
    
    @classmethod
    def all_roles(cls):
        return [cls.ADMIN, cls.INSTRUCTOR, cls.STUDENT]

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    role = db.Column(db.String(20), nullable=False, default=Role.STUDENT)
    profile_image_url = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    courses_created = db.relationship('Course', backref='instructor', lazy=True, 
                                     cascade="all, delete-orphan")
    enrollments = db.relationship('Enrollment', backref='student', lazy=True,
                                 cascade="all, delete-orphan")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def is_admin(self):
        return self.role == Role.ADMIN
    
    def is_instructor(self):
        return self.role == Role.INSTRUCTOR
    
    def is_student(self):
        return self.role == Role.STUDENT
    
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    def __repr__(self):
        return f'<User {self.username}>'

class Course(db.Model):
    __tablename__ = 'courses'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    code = db.Column(db.String(20), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    is_active = db.Column(db.Boolean, default=True)
    max_students = db.Column(db.Integer, default=50)
    thumbnail_url = db.Column(db.String(500), nullable=True)  # New field for course thumbnail
    
    # Relationships
    enrollments = db.relationship('Enrollment', backref='course', lazy=True,
                                 cascade="all, delete-orphan")
    videos = db.relationship('CourseVideo', backref='course', lazy=True,
                           cascade="all, delete-orphan")
    
    def get_enrollment_count(self):
        return len(self.enrollments)
    
    def is_full(self):
        return self.get_enrollment_count() >= self.max_students
    
    def __repr__(self):
        return f'<Course {self.title}>'

class Enrollment(db.Model):
    __tablename__ = 'enrollments'
    
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')  # active, completed, dropped
    
    # Ensure a student can only enroll in a course once
    __table_args__ = (
        db.UniqueConstraint('student_id', 'course_id', name='uq_student_course'),
    )
    
    def __repr__(self):
        return f'<Enrollment {self.student_id} in {self.course_id}>'

class CourseVideo(db.Model):
    __tablename__ = 'course_videos'
    
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    video_type = db.Column(db.String(20), nullable=False)  # 'youtube' or 'upload'
    video_url = db.Column(db.String(500), nullable=False)  # YouTube URL or uploaded file path
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.Column(db.Integer, default=0)  # For ordering videos in the course
    
    def __repr__(self):
        return f'<CourseVideo {self.title}>'
