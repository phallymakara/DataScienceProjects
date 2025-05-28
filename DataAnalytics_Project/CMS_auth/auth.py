from functools import wraps
from flask import flash, redirect, url_for, request
from flask_login import current_user
from models import Role

def role_required(*roles):
    """
    Decorator that checks if the current user has at least one of the specified roles.
    Usage: @role_required(Role.ADMIN, Role.INSTRUCTOR)
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                flash('Please log in to access this page.', 'warning')
                return redirect(url_for('login', next=request.url))
            
            if current_user.role not in roles:
                flash('You do not have permission to access this page.', 'danger')
                return redirect(url_for('index'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def admin_required(f):
    """Decorator that checks if the current user is an admin."""
    return role_required(Role.ADMIN)(f)

def instructor_required(f):
    """Decorator that checks if the current user is an instructor."""
    return role_required(Role.ADMIN, Role.INSTRUCTOR)(f)

def instructor_or_admin_required(f):
    """Decorator that checks if the current user is an instructor or admin."""
    return role_required(Role.ADMIN, Role.INSTRUCTOR)(f)
