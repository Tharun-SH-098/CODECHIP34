print("To check whether the string is alphanumeric")
str1="abcd1234"
print(str1.isalnum())

print("To check whether the string is completely alphabets")
str2="Programming"
print(str2.isalpha())

print("To check whether the string is including only didgits")
str3="45"
print(str3.isdigit())

print("To check whether the string is space")
str4=" "
print(str4.isspace())

str5="WE Are Learning Python"
print(str5.istitle())

print("To check whether the string is in upper case or lower case")
str6="We are learning Python"
print(str6.islower())
print(str6.isupper())

print("to check whether the string is in upper case or lower case")
str7="I LOVE LEARNING PYTHON"
print(str7.isupper())
print(str7.islower())

print("to replace the old string with new string")
str8="I love to learn Python"
print(str8.replace("I","We"))

print("To count the occurance of the string")
str10="I am executing python program "
print(str10.count('g'))

print("To find the first occurance of the string")
str10="I am executing python program "
print(str10.find('g'))

print("To convert the string from one case to another case")
str11="hello world"
print(str11.swapcase())
print(str7.swapcase())

print("To check whether string starts with given string")
str12="water is very very precious"
print(str12.startswith('water'))

print("To check wherther string ends with given string")
print(str12.endswith('precious'))

print("To capitalize th first character of the string")
str13="hello world"
print(str13.capitalize())

print("To convert the string to upper case")
str14="Hello world"
print(str14.upper())

print("To convert the string to lower case")
str14="HELLO WORLD"
print(str14.lower())

print("To remove the spaces from the string")
str15="    Python Program    "
print(str15.strip())
print(str15.lstrip())
print(str15.rstrip())

print("To display the string with special characters")
str16="Python"
print(str16.center(20,'*'))
print(str16.ljust(20,'*'))
print(str16.rjust(20,'*'))

l=['We','are','learning','python']
s=''
print(s.join(l))

s="we are learning python"
s1=s.split(' ')
print(s1)

