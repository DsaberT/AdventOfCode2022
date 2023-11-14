"""with open('input.txt', 'r') as file:
    lines = file.readlines()
    

cycle = 1
addx = 1
sum = 0

for line in lines:
    command = line.strip()
    if command.startswith("noop"):
        cycle += 1
    else:
        cycle += 1
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
           sum += addx*cycle
           print("Here is  the cycle: ", addx*cycle)
        cycle += 1
        addx += int(command.split(" ")[1])
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        sum += addx*cycle
        print("Here is  the cycle: ", addx*cycle)
    #print(addx)
print(sum)"""





instructions = open("input.txt").readlines()

x = 1
c = 0
hist = [x]
output = ""

pix = lambda c, x: "#" if abs(c - x) <= 1 else "."

for instr in instructions:
    output += pix(c, x)
    print(output)
    print(instr)
    c = (c + 1) % 40
    if instr.startswith("addx"):
        output += pix(c, x)
        print(output)
        print(instr)
        c = (c + 1) % 40
        hist.append(x)
        x += int(instr.split()[1])
    hist.append(x)

print(sum(i*hist[i-1] for i in range(20, 221, 40)))
for row in range(0, 6):
    print(output[row*40:(row+1)*40])