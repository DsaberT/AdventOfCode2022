import re
with open('input.txt', 'r') as file:
    lines = file.readlines()


monkey = []
MonkeyOper = []
operands = []
divider = []
iftrue = []
iffalse = []
collection =[]


for line in lines:
    command = line.strip()
    if command.startswith("Starting"):
        monkey.append((re.split(r'[,\s]+', command))[2:])          # making sure we only have the items left

    if command.startswith("Operation"):
        MonkeyOper.append(command.split(" ")[5])
        operands.append(command.split(" ")[4])

    if command.startswith("Test"):
        divider.append(command.split(" ")[3])
    
    if command.startswith("If true:"):
        iftrue.append(command.split(" ")[5])
    
    if command.startswith("If false:"):
        iffalse.append(command.split(" ")[5])

collection = [0]* len(monkey)

#For part 2
product = 1
for dividers in divider:
    product *= int(dividers)
    

for _ in range(0, 10000):
    for i in range(len(monkey)):
        for k in range(len(monkey[i])):
            if MonkeyOper[i] == "old":                  
                temp = monkey[i][k]
            else:
                temp = MonkeyOper[i]
        
            if operands[i] == "*":                      
                item = int(monkey[i][k]) * int(temp)
            else:
                item = int(monkey[i][k]) + int(temp)
            
            #item = int(item / 3) #Part 1
            
            item = item % product   #for part 2
            
            if item % int(divider[i]):
                monkey[int(iffalse[i])].append(item)
    
            else:
                monkey[int(iftrue[i])].append(item)
            
            collection[i] += 1
        
        if len(monkey[i]) > 0:
            for j in range(0, k + 1):
                monkey[i].pop(0)  

max1 = max(collection)
collection.remove(max1)
max2 = max(collection)

print(max1*max2)

