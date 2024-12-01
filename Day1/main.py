
with open('input.txt', 'r') as file:
    input = file.readlines()

cord1 = []
cord2 = []

for line in input:
    split = line.split()
    cord1.append(int(split[0]))
    cord2.append(int(split[1]))

cord1.sort()
cord2.sort()

sum = 0

for i in range(0,len(cord1)):
    diff = abs(cord1[i] - cord2[i])
    sum += diff

print(f"distance: {sum}")

similarity_sum = 0
for i in range(0,len(cord1)):
    count = cord2.count(cord1[i])
    if count != 0:
        similarity_sum += cord1[i]*count

print(f"similarity_sum: {similarity_sum}")