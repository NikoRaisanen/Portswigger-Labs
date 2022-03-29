# Script to convert passwords.txt into list format
passwords = []
passwords2 = []
with open('../passwords.txt', 'r') as fp:
    passwords = fp.readlines()

for pw in passwords:
    passwords2.append(pw.strip())

for pw in passwords2:
    # print with double quotes and comma
    print(f'"{pw}",')