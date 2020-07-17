import re

text_to_search = """
+1 206-494-1685

801 431 4900
+1 267 846 2671
321-545-2312
123.555.1234

johnwilliams@bogusemail.com
johnwil.liams@bogusemail.com
johnwilliams34@bogusemail.com
johnwil44liams@bogusemail.com
jksd@gmail.com
"""
phone_number_pattern = r"\d{3}[\s.-]\d{3}[\s.-]\d{4}|\+\d{1,2}\s\d{3}[\s.-]\d{3}[\s.-]\d{4}"
phones = re.findall(phone_number_pattern,text_to_search)
print("Phones : ",phones)
email_pattern = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"
emails = re.findall(email_pattern,text_to_search)
print("Emails : ",emails)
