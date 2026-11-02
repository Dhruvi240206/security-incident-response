import os

USERNAME = "admin"
PASSWORD = os.getenv("APP_PASSWORD")

def login(username, password):
    if username == USERNAME and password == PASSWORD:
        return "Login successful"
    else:
        return "Invalid credentials"

print(login("admin", "TestPassword123"))