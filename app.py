# Simulated vulnerable application

USERNAME = "admin"
PASSWORD = "TestPassword123"

def login(username, password):
    if username == USERNAME and password == PASSWORD:
        return "Login successful"
    else:
        return "Invalid credentials"

print(login("admin", "TestPassword123"))