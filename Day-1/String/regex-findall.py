# Regex Findall

import re

text = "The Lion is brave, the Lion is the King"
pattern = r"Lion"

search = re.findall(pattern, text)
if search:
    print("Pattern found:", search, "Count:", search.count("Lion")) 
else:
    print("Pattern not found")

