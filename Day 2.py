f = open("Day 2.txt", "r")
file = []
for line in f:
    file.append(line.replace("\n", ""))

truePasswords = 0

for x in range(1000):
    policyLetter = file[x].split(":")[0][-1]
    password = file[x].split(':')[1]
    numCount = password.count(policyLetter)
    min = int(file[x].split(":")[0].split("-")[0])
    max = int(file[x].split(":")[0].split("-")[1].split(" ")[0])

    if min <= numCount <= max:
        truePasswords += 1


print(truePasswords)


truePasswords = 0

for x in range(1000):
    policyLetter = file[x].split(":")[0][-1]
    password = file[x].split(':')[1]
    numCount = password.count(policyLetter)
    min = int(file[x].split(":")[0].split("-")[0])
    max = int(file[x].split(":")[0].split("-")[1].split(" ")[0])

    if min <= numCount <= max:
        truePasswords += 1


print(truePasswords)
