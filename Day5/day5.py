file = open('input.txt', 'r')
Lines = file.readlines()

list = ["","","","","","","","",""]

skip = 0
temp1 = 0
#---------------------------------Part 1----------------------------------------
for line in Lines:
    if (len(line)) == 36 and skip < 8:
        coloumn = 0
        for x in range(1,len(line)+1, 4):
            if line[x] != " ":
                temp = list[coloumn]
                list[coloumn] = str(list[coloumn]+str(line[x]))     
            coloumn +=1
        skip += 1
    else:
        if skip == 9:
            line = line.replace("move ", "")
            line = line.replace("from ", "")
            line = line.replace("to ", "")
            line = line.replace("\n", "")
            line = line.split(" ")
            for i in range(0, len(line), 1):
                if i == 0 and line[i] != "":
                    temp1 = (line[i])
                elif i == 1:
                    temp2 = (line[i])
                elif i == 2:
                    temp3 = (line[i])
            
            for k in range(0, int(temp1), 1):
                temp = (list[int(temp2)-1])[0]
                list[int(temp2)-1] = (list[int(temp2)-1])[1:]
                list[int(temp3)-1] = str(temp) + str(list[int(temp3)-1])
        else:
            skip += 1
string = ""
for i in range(0,9,1):
    temp = (list[i])[0]
    string = str(string) +str(temp)
print(string)

skip = 0
temp1 = 0
#-----------------------------Part 2----------------------------

for line in Lines:
    if (len(line)) == 36 and skip < 8:
        coloumn = 0
        for x in range(1,len(line)+1, 4):
            if line[x] != " ":
                temp = list[coloumn]
                list[coloumn] = str(list[coloumn]+str(line[x]))     
            coloumn +=1
        skip += 1
    else:
        if skip == 9:
            line = line.replace("move ", "")
            line = line.replace("from ", "")
            line = line.replace("to ", "")
            line = line.replace("\n", "")
            line = line.split(" ")
            for i in range(0, len(line), 1):
                if i == 0 and line[i] != "":
                    temp1 = (line[i])
                elif i == 1:
                    temp2 = (line[i])
                elif i == 2:
                    temp3 = (line[i])
            
            test = ""
            solve =""
            
            for k in range(0, int(temp1), 1):
                temp = (list[int(temp2)-1])[0]
                #print("before removal: "+ str(list[int(temp2)-1]))
                solve = (list[int(temp2)-1])[1:]
             
                list[int(temp2)-1] = solve
                
                #print("this is the list: " +str(list[int(temp2)-1])+ " this is the minus 1: " + str(solve))
                if int(temp1) == 0:
                    test = str(temp)
                else:
                    test = str(test) + str(temp)
            print("this is the length of temp1: " + str(temp1))
            print("This is the before the updated: " + str(list[int(temp3)-1]) + " this is the temp: " +str(test))
            list[int(temp3)-1] = str(test) + str(list[int(temp3)-1])
            print("This is the updated: " + str(list[int(temp3)-1]))
                
        else:   
            skip += 1
string = ""
print(list)
for i in range(0,9,1):
    temp = (list[i])[0]
    string = str(string) +str(temp)
print(string)
