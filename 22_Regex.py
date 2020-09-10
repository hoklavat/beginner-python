#22- Regular Expressions

import re

mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP."
#a = re.match("You", mystr)
a = re.match("you", mystr, re.I)
print(a)
print(a.group())

arp = "22.22.22.1 0     b4:a9:5a:ff:c8:45 VLAN#222    L"
a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
print(a.group(0))
print(a.groups())
print(a.group(1))
print(a.group(2))
print(a.group(3))
print(a.group(4))

a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
print(a)
print(type(a))
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(a)

arp = "22.22.22.1 0     b4:a9:5a:ff:c8:45 VLAN#222  10.10.10.23  L"
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(a)

b = re.sub(r"\d", "7", arp)
print(b)