from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, BooleanField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError, Optional
from models import User, Role

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Please enter a valid email address."),
        Length(min=5, max=120, message="Email must be between 5 and 120 characters long.")
    ])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[Optional(), Length(max=50)])
    last_name = StringField('Last Name', validators=[Optional(), Length(max=50)])
    role = SelectField('Role', choices=[(Role.STUDENT, 'Student'), (Role.INSTRUCTOR, 'Instructor')], default=Role.STUDENT)
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken. Please choose a different one.')
    
    def validate_email(self, email):
        # Check if email already exists
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already registered. Please use a different one.')
        
        # Check email domain
        email_domain = email.data.split('@')[1].lower()
        disposable_domains = ['tempmail.com', 'temp-mail.org', 'throwawaymail.com']
        if email_domain in disposable_domains:
            raise ValidationError('Disposable email addresses are not allowed. Please use a valid email address.')

class UserUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[Optional(), Length(max=50)])
    last_name = StringField('Last Name', validators=[Optional(), Length(max=50)])
    role = SelectField('Role', choices=[(role, role.capitalize()) for role in Role.all_roles()])
    profile_image = FileField('Profile Image', validators=[
        Optional(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])
    profile_image_url = StringField('Profile Image URL', validators=[Optional()], 
                                  description='If no image is uploaded, you can provide a URL instead')
    submit = SubmitField('Update')
    
    def __init__(self, original_username, original_email, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is already taken. Please choose a different one.')
    
    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is already registered. Please use a different one.')

class CourseForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description')
    code = StringField('Course Code', validators=[DataRequired(), Length(max=20)])
    start_date = DateField('Start Date', validators=[Optional()])
    end_date = DateField('End Date', validators=[Optional()])
    is_active = BooleanField('Active', default=True)
    max_students = IntegerField('Maximum Students', default=50)
    thumbnail = FileField('Course Thumbnail', validators=[
        Optional(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
    ])
    thumbnail_url = StringField('Thumbnail URL', validators=[Optional(), Length(max=500)],
                              description='URL to an image that represents this course')
    submit = SubmitField('Save Course')
    
    def __init__(self, original_code=None, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        self.original_code = original_code
    
    def validate_code(self, code):
        from models import Course
        if self.original_code is None or code.data != self.original_code:
            course = Course.query.filter_by(code=code.data).first()
            if course:
                raise ValidationError('That course code is already in use. Please choose a different one.')

class CourseVideoForm(FlaskForm):
    title = StringField('Video Title', validators=[DataRequired(), Length(max=200)])
    video_type = SelectField('Video Type', 
                           choices=[('youtube', 'YouTube Video'), ('upload', 'Upload Video')],
                           validators=[DataRequired()])
    video_url = StringField('Video URL/Path', validators=[DataRequired(), Length(max=500)])
    description = TextAreaField('Description')
    order = IntegerField('Display Order', default=0)
    submit = SubmitField('Add Video')

class EnrollmentForm(FlaskForm):
    submit = SubmitField('Enroll in Course')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired()])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Change Password')
