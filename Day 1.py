f = open("Day 1.txt", "r")
file = []
for line in f:
    file.append(int(line.replace("\n", "")))

# print(2020 - file[1])


for x in range(200):
    for y in range(200):
        if (2020 - file[x] - file[y]) in file:
            print(file[x])
print(395*198*1427)
