import re
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
extract_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
example_text = "Contact us at info@example.com or support@company.com for assistance."
extracted_emails = re.findall(extract_pattern, example_text)
print("Extracted Email Addresses:")
for email in extracted_emails:
    print(email)
print("\nValidation:")
for email in extracted_emails:
    valid = bool(re.match(email_pattern, email))
    print(f"{email}: {valid}")
