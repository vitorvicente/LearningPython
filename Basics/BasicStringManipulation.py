#  String manipulation
print("Basic String Manipulation:")
print("s1 = 'Hello World'\n")

s1 = "Hello World"

print("s1[0] =", s1[0])
print("len(s1) =", len(s1))
print("s1.count('l') =", s1.count('l'))
print("s1.find('e') =", s1.find('e'))
print("s1[:-5] =", s1[:-5])
print("s1.split(' ') =", s1.split(' '))
print("s1*2 =", s1*2)

#  Caps String manipulation
print("\nCaps String Manipulation:")
print("s2 = 'hello there' AND s3 = 'HEY' AND s4 = 'hEy'  \n")

s2 = "hello there"
s3 = "HEY"
s4 = "hEy"

print("s2.upper() =", s2.upper())
print("s3.lower() =", s3.lower())
print("s2.title() =", s2.title())
print("s4.swapcase() =", s4.swapcase())
print("s2.capitalize() =", s2.capitalize())

#  String Content manipulation
print("\nString Content Manipulation:")
print("s5 = '01234' AND s6 = '56789' \n")

s5 = "01234"
s6 = "56789"

print("s5.replace('1', '0') =", s5.replace('1', '0'))
print("''.join(reversed(s5)) =", ''.join(reversed(s5)))
print("s5.strip() =", s5.strip())
print("s5.lstrip() =", s5.lstrip())
print("s5.rstrip() =", s5.rstrip())
print("s5 + s6 =", s5 + s6)
print("' '.join(s5) =", ' '.join(s5))

#  String Content manipulation
print("\nString Testing:")
print("s7 = 'Complete String' \n")

s7 = "Complete String"

print("s7.startswith('H') =", s7.startswith('H'))
print("s7.endswith('g') =", s7.endswith('h'))
print("s7.isalnum =", s7.isalnum())
print("s7.isalpha =", s7.isalpha())
print("s7.isdigit =", s7.isdigit())
print("s7.istitle =", s7.istitle())
print("s7.isupper =", s7.isupper())
print("s7.islower =", s7.islower())
print("s7.isspace =", s7.isspace())
