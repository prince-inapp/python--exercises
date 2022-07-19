import re
phrase = 'They ate 6 apples and 10 banana'
sub1 = re.sub('6', 'six', phrase)
sub2 = re.sub('10', 'ten', sub1)
print(sub2)