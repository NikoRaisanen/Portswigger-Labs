# Create payloads for passwords and usernames to use in Burp Intruder Pitchfork attack
# Run 2 lists in parallel -- newPW.txt and newUSER.txt
# This script generates those 2 files
passwords = []
newPW = []
with open('passwords.txt', 'r') as fp:
    passwords = fp.readlines()

for i in range(len(passwords)):
    newPW.append(passwords[i])
    if i%2 == 0:
        newPW.append('peter\n')

with open('newPW.txt', 'w') as fp:
    fp.writelines(newPW)

with open('newUSER.txt', 'w') as fp:
    userList = []
    for pw in newPW:
        if pw == 'peter\n':
            userList.append('wiener\n')
        else:
            userList.append('carlos\n')

    fp.writelines(userList)
