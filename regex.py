import re

string = "I AM NOT YELLING, she said. Though we knew it not to be true"

new = re.sub('[A-Z]', '', string)

print(new)