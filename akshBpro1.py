import re
text="Hello,World!"
pattern=r"HELLO"
match=re.search(pattern,text)
if match:
    print("Pattern found!")
else:
    print("Pattern not found")
text="There is a rain in spain"
pattern=r"ai"
matches=re.findall(pattern,text)
print("The list containing every occurance of given pattern",matches)
print("Number of occurances:",len(matches))
text="My email is john@example.com"
pattern=r"(\w+)@(\w+)\.com"
match=re.search(pattern,text)
if match:
    username=match.group(1)
    domain=match.group(2)
    print("Username:",username)
    print("Domain:",domain)
