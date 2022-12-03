file = open('Items.txt', 'r')
Lines = file.readlines()

Alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = 0


#-------------Part 1-------------
for line in Lines:
    #using floor division in the case we have even or odd items 
    Half = len(line)//2 
    #creat two sets then look for intersection between them
    leftside = line[0:Half]
    rightside = line[Half:len(line)]
    Items = set(leftside).intersection(set(rightside))
    
    #Match the value to the alphabetic value
    temp = Items.pop()
    i = 0
    while i < len(Alpha):        
        if temp == Alpha[i]:
            points += (i+1)
            i = len(Alpha)
        else:
            i+=1
print("This is the answer for the first question: " + str(points))

#----------Part 2------------
points = 0
for i in range(0, (len(Lines) - 1), 3):
   
    Member1 = Lines[i].strip()
    Member2 = Lines[i+1].strip()
    Member3 = Lines[i+2].strip()
    Members = [Member1,Member2,Member3]

    #see what item is common between the group members
    Badge = set(Members[0]).intersection(set(Members[1])).intersection(set(Members[2]))
   
    #Use the same method as before in part 1
    temp = Badge.pop()
    i = 0
    while i < len(Alpha):        
        if temp == Alpha[i]:
            points += (i+1)
            i = len(Alpha)
        else:
            i+=1
print("The answer to question 2 is: "+str(points))