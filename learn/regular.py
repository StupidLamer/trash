import re

# s = 'This is just string. And it is string too'
# pattern = 'string'

# match = re.search(pattern, s)
# print(match.start())
# print(match.end())

# print(re.findall(pattern, s))

# print(re.split(r'\. ', s))

# s = '''This is just string.
# And it is string too.
# And it is string with numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 10
# And it is string with chars: "!", "@", "-", "&", "?", "_"
# a\\b\tc
# test string'''

# pattern = r'\w+'
# pattern = r'[a-z]+'
# pattern = r'[0-9]+'
# pattern = r'\d+'
# pattern = r'[\da-]'
# pattern = r'a\\b\tc'

# pattern = r'^\w+'

# print(re.findall(pattern, s, flags=re.IGNORECASE))

# mail@mail.com
# mail@bank
# mail@google.com.uk
# def validate_email(mail):
# 	return re.match(r'^.+@(\w+\.){0,2}[a-z]{2,6}$', mail, re.IGNORECASE)

# print(validate_email('mail@mail.com'))
# print(validate_email('mail@bank'))
# print(validate_email('mail@google.com.uk'))