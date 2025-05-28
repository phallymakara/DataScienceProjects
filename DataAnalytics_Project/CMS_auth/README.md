# Course Management System (CMS)

A web-based course management system built with Flask that allows instructors to create and manage courses, and students to enroll in courses.

## Features

- **User Management**
  - User registration and authentication
  - Role-based access control (Admin, Instructor, Student)
  - Profile management

- **Course Management**
  - Create and edit courses
  - Upload course thumbnails
  - Add course videos
  - Set course capacity and status

- **Enrollment System**
  - Students can enroll in courses
  - Enrollment status tracking
  - Course capacity management

- **Administrative Features**
  - User management
  - Course oversight
  - System statistics

## Technology Stack

- **Backend**: Python/Flask
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Frontend**: Bootstrap, JavaScript
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **File Upload**: Werkzeug

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd CMS_auth
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Unix
# or
venv\Scripts\activate     # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
flask db upgrade
```

6. Run the application:
```bash
flask run
```

## Deployment on Render

This application can be easily deployed to Render.com by following these steps:

1. Create a [Render account](https://render.com) if you don't have one

2. Create a new PostgreSQL database in Render:
   - Go to Dashboard > New > PostgreSQL
   - Provide a name for your database
   - Select a suitable plan
   - Note your database connection details for use in the environment variables

3. Create a new Web Service in Render:
   - Go to Dashboard > New > Web Service
   - Connect your GitHub repository
   - Fill in the following details:
     - **Name**: Your application name
     - **Environment**: Python 3
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn -c gunicorn.conf.py main:app`
     - **Branch**: main (or your deployment branch)

4. Set the environment variables under the "Environment" tab:
   - `FLASK_APP`: main.py
   - `FLASK_ENV`: production
   - `SECRET_KEY`: (generate a secure random key)
   - `WTF_CSRF_SECRET_KEY`: (generate a secure random key)
   - `DATABASE_URL`: (use the Internal Database URL from your PostgreSQL service)

5. Enable automatic deploys if desired

6. Click "Create Web Service" and Render will build and deploy your application

Your application will be available at your Render-provided URL once the deployment process completes.

## Project Structure

```
CMS_auth/
├── app.py              # Flask application initialization
├── config.py           # Configuration settings
├── models.py           # Database models
├── forms.py            # Form classes
├── routes.py           # Route handlers
├── static/            
│   └── uploads/        # Uploaded files
├── templates/          # HTML templates
├── migrations/         # Database migrations
└── requirements.txt    # Project dependencies
```

## Database Schema

### Users Table
- id (Primary Key)
- username (Unique)
- email (Unique)
- password_hash
- role (admin/instructor/student)
- profile_image_url
- created_at
- updated_at

### Courses Table
- id (Primary Key)
- title
- description
- instructor_id (Foreign Key)
- code (Unique)
- thumbnail_url
- max_students
- is_active
- created_at
- updated_at

### Enrollments Table
- id (Primary Key)
- student_id (Foreign Key)
- course_id (Foreign Key)
- status
- enrolled_at

### Course Videos Table
- id (Primary Key)
- course_id (Foreign Key)
- title
- video_type
- video_url
- order
- created_at

## Role-Based Access

1. **Admin**
   - Manage all users
   - Manage all courses
   - View system statistics
   - Full system access

2. **Instructor**
   - Create and manage own courses
   - Add course content
   - View enrolled students
   - Manage course videos

3. **Student**
   - View available courses
   - Enroll in courses
   - Access course content
   - View enrollment history

## Security Features

- Password hashing
- CSRF protection
- Session management
- Role-based access control
- Secure file uploads
- Input validation

## Development

To contribute to this project:

1. Create a new branch
2. Make your changes
3. Submit a pull request

## Testing

Run tests using:
```bash
python -m pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 