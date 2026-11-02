import re

file_name = "app.py"

with open(file_name, "r") as file:
    content = file.read()

patterns = [
    r'PASSWORD\s*=\s*["\'].*?["\']',
    r'API_KEY\s*=\s*["\'].*?["\']',
    r'SECRET_KEY\s*=\s*["\'].*?["\']'
]

found = False

for pattern in patterns:
    matches = re.findall(pattern, content)

    if matches:
        found = True
        print("SECURITY ALERT: Hardcoded secret detected!")
        print("Issue found in:", file_name)

if found:
    print("Inspection result: Vulnerability detected.")
    exit(1)

print("Inspection result: No hardcoded secrets detected.")