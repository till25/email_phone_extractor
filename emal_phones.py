import re


output = """
Get In Touch

1875 South State Street Suite 3000
Orem, UT 84097

Phone: 801-431-4900

Moderator
moderator@mlm.com

Editor
editor@mlm.com
The Direct Sales Resource

MLM.com is wholly owned and published by InfoTrax Systems. The opinions expressed by bloggers and forum participants are their own and not the responsibility of InfoTrax Systems, its employees or management team. MLM.com makes every effort to monitor the content of this site but does not warrant or endorse any company, individual or their opinions expressed herein. MLM.com encourages lively conversation and debate but prohibits any disparaging of individuals or institutions, except as appropriate in professional criticism and reportage. Report any abuses you suspect to MLM.com.

"""
#regular expression to find emails
emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", output)
#regular expression to find phone numbers
numbers = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', output)

print(numbers)
print(emails)

for email in emails:
	print('EMAIL :-> ' + email)
	F = open('emails.json','a+')
	F.write('EMAIL :-> ' + email)

for number in numbers:
	print('Phone No. :-> ' + number)
	F = open('emails.json', 'a+')
	F.write('\n Phone No. :-> ' + number)