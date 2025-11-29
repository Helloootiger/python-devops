# Regex search

import re

text = "The Lion is brave, the Lion is the King"
pattern = r"Lion"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")

