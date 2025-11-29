# Regex Match

import re

text = "The brave Lion"
pattern = r"Lion"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("Match not found")

#Output will be "Match not found" - beacuse match will look for the start string, here "The" is the start of the string