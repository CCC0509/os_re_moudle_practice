import os
import re


result = []


def search(st):
    r = re.findall(r"\d{3}-\d{3}-\d{4}", st)
    if r:
        for number in r:
            result.append(number)


for path, folder, file in os.walk("Employee"):
    for f in file:
        with open(os.path.join(path, f)) as my_file:
            text = my_file.read()
            search(text)

print(result)
