import re

# Read resume text from a text file
file_path = 'static/uploads/Resumewords.txt'
try:
    with open(file_path, 'r') as file:
        resume_text = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
    exit()

patternL = r"\b(\d+)[+\s]*(?:years?|yrs?)\b"
matchesL = re.findall(patternL, resume_text, re.IGNORECASE)

if matchesL:
    print("Years of experience found in the resume:")
    for years in matchesL:
        print("- " + years)
else:
    print("No years of experience found in the resume.")
    job_level_match = "Fresher"
