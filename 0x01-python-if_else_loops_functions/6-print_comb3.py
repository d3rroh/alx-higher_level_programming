#!/usr/bin/python3
for j in range(0, 89):
    if j / 10 < j % 10:
        print("{:02d}, ".format(j), end='')
print(89)
