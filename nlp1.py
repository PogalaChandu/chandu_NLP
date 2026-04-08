import re

text = "My phone number is 9876543210 and email is test@gmail.com"

phone_pattern = r'\d{10}'
phone = re.search(phone_pattern, text)

if phone:
    print("Phone:", phone.group())

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}'
email = re.search(email_pattern, text)

if email:
    print("Email:", email.group())