file = open('input.txt', 'r')
Lines = file.readlines()

SameWork1 = 0
SameWork2 = 0

for line in Lines:
    line = line.split()            #take away the \n
    line = line[0].split(',')      #take away the comma, Seperated to two lists now
    Left = line[0].split('-')      #the first work assignments is collected on one list
    Right = line[1].split('-')     #while the other on the other side to compare


#---------------------PART 1--------------------------
    SpecialcaseFlag = 0
    if int(Left[0]) <= int(Right[0]):               #if leftsides first assignment is lower then right
        if int(Left[1]) >= int(Right[1]):           #if leftsides last assignment is bigger then right
            SameWork1 += 1                          # rightside is inside leftside
            SpecialcaseFlag = 1 

    if ((int(Left[0]) >= int(Right[0])) and SpecialcaseFlag == 0):  #inverted of the other if to see if left in right
        if int(Left[1]) <= int(Right[1]):
            SameWork1 += 1

#------------------------Part 2--------------------------------
    SpecialcaseFlag = 0
    if int(Left[0]) <= int(Right[0]):
        if int(Left[1]) >= int(Right[0]):
            SameWork2 += 1
            SpecialcaseFlag = 1

    if ((int(Left[0]) >= int(Right[0])) and SpecialcaseFlag == 0):
        if int(Left[0]) <= int(Right[1]):
            SameWork2 += 1

print("This is the result for part 1: " + str(SameWork1))
print("This is the result for part 2: " + str(SameWork2))