# Regex Replace

import re

text = "The brave Lion is the King of Jungle"
pattern = r"Jungle"

replacement = "Forest"

new_text = re.sub(pattern, replacement, text)
print("Modified text:", new_text)