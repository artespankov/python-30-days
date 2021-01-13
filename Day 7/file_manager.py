import os

this_file_path = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)

print(this_file_path)
print(BASE_DIR)
print(ENTIRE_PROJECT_DIR)

email = os.path.join(BASE_DIR, "templates", "email.txt")


with open(email, 'r') as f:
    content = f.read()

print(content.format(name='Art'))
