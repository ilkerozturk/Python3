import re
from unittest import result   # Import the regular expression module

str = "Python Kursu: Python uygulamalı yazılım geliştirme kursu"

# Find all occurrences of the word "Python" in the string
"""result = re.findall("Python", str)
print(result)  # Output: ['Python', 'Python']
print(type(result))  # Output: <class 'list'>   
print(len(result))  # Output: 2
print(result[0])  # Output: Python
print(result[1])  # Output: Python
"""


#result = re.split(" ", str)  # Split the string by spaces   
#print(result)  # Output: ['Python', 'Kursu:', 'Python', 'uygulamalı', 'yazılım', 'geliştirme', 'kursu']

#result = re.sub(" ", "-", str)  # Replace spaces with hyphens
#print(result)  # Output: Python-Kursu:-Python-uygulamalı-yazılım-geliştirme-kursu

result = re.match("Python", str)  # Check if the string starts with "Python"

print(result)  # Output: <re.Match object; span=(0, 6), match='Python'>
print(result.span())  # Output: (0, 6)
print(result.start())  # Output: 0
print(result.end())  # Output: 6
print(result.group())  # Output: Python
print(result.string)  # Output: Python Kursu: Python uygulamalı yazılım geliştirme kursu