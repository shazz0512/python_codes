# import re

# email_pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b'
# text= 'Contact us at support@gmail.com and wite is info@doorstep.com'
# matches=re.findall(email_pattern,text)
# print(matches)


import re

string="Hello to the world of python ,python is the easy languague"
print(string)
pattern="python"

matches=re.search(pattern,string,re.IGNORECASE)
print(matches)
# if matches in string:
#     print("match found")
# else:
#     print('no match')
    
    
string="Hello to the world of python ,python is the easy languague"
print(string)
pattern="python"
replacement="Java"

matches=re.sub(pattern,replacement,string,re.IGNORECASE)
print(matches)    
    