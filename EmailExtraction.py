import re
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
text = ("Hello! I am Nithin Sai, Welcome to my blog. For any queries you can contact me at mobile:9014438688 or email: nithinsai@gmail.com")
email_addresses = re.findall(email_pattern, text)
if email_addresses:
    print("Found email address is:")
    for email in email_addresses:
        print(email)
else:
    print("No valid email addresses found.")
