import re

text = "156889808881"
reg = re.match("1[3456789]")
print(reg.group())
