# Regex Split

import re

text = "Lion,Tiger,Fox,Bear"
pattern = r","

split_text = re.split(pattern, text)
print("Splited text:", split_text)

