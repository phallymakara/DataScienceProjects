import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(32)
csrf_key = secrets.token_hex(32)

print("Add these lines to your .env file:\n")
print(f"SECRET_KEY={secret_key}")
print(f"WTF_CSRF_SECRET_KEY={csrf_key}") 