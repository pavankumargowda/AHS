import re

def find_education_match(jd_text, resume_text):
    jd_qualifications = extract_qualifications(jd_text)
    resume_qualifications = extract_qualifications(resume_text)

    matched_qualifications = []
    for jd_qualification in jd_qualifications:
        for resume_qualification in resume_qualifications:
            if jd_qualification.lower() == resume_qualification.lower():
                matched_qualifications.append(resume_qualification)

    return matched_qualifications

def extract_qualifications(text):
    pattern = r"(?i)\b(?:education|qualification|degree)\b(?:.*?\b(?:in|from)\b)?\s*([a-zA-Z\s]+)"
    matches = re.findall(pattern, text)
    qualifications = [match.strip() for match in matches]
    return qualifications

# Example usage
jd_text = """
We are looking for a candidate with the following qualifications:
- Bachelor's degree in Computer Science or a related field
- Master's degree is a plus
"""

resume_text = """
I have a Bachelor's degree in Computer Science from XYZ University.
Prior to that, I completed my high school education at ABC School.
"""

matched_educations = find_education_match(jd_text, resume_text)

if matched_educations:
    print("Matched education qualifications:")
    for qualification in matched_educations:
        print("- " + qualification)
else:
    print("No matched education qualifications found.")
