import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x.start())
print(x.string)

x = re.findall("ai", txt)
y = re.findall("zzz", txt)
print(x, y)

x = re.split("\s", txt)
print(x)

x = re.split("\s", txt, 1)
print(x)

x = re.sub("\s", "9", txt)
print(x)
