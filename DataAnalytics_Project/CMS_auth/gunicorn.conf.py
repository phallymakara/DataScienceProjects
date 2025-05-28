import multiprocessing

# Gunicorn configuration for Render deployment
bind = "0.0.0.0:10000"  # Render will set PORT env var, this is a fallback
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
worker_class = "gthread"
worker_connections = 1000
timeout = 30
keepalive = 2
accesslog = "-"  # Log to stdout for Render logging
errorlog = "-"   # Log to stderr for Render logging
loglevel = "info" 