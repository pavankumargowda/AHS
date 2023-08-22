import re

resume_text = ""

# Read resume text from a text file
file_path = 'static/uploads/Resumewords.txt'
try:
    with open(file_path, 'r') as file:
        resume_text = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    exit()

phone_number = re.search(r'\d+', resume_text)
email_match = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', resume_text)

email = email_match.group(0) if email_match else None

if phone_number:
    phone_number = phone_number.group(0)
    print("Phone number:", phone_number)
else:
    print("Phone number not found in the resume.")

if email:
    # Remove the trailing "Email" text from the email string
    email = email.replace("Email", "")
    print("Email:", email)
else:
    print("Email not found in the resume.")