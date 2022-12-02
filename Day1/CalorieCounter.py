file = open('ElfCalories.txt', 'r')
Lines = file.readlines()


Calories = 0
MaxCalories = [0,0,0]
Total = 0

for Line in Lines:
    Lina = Line.rstrip()
    #print(Lina)
    if Lina != ("") :
        Calories += int(Lina)
    elif Lina == (""):
        i = int(0) 
        k = int(0)
        while i < 3:           
            if int(MaxCalories[i])< Calories:
                temp = MaxCalories[i]
                MaxCalories[i] = Calories
                print("Detta är i " + str(i))
                if i < 3:
                    k=i+1
                    i=3
                    print("Det är k = i+1 " + str(k))
                    while k < 3:
                        #print(str(temp))
                        #print(str(MaxCalories[k]))
                        if int(MaxCalories[k]) < temp:
                            temp2 = MaxCalories[k]
                            MaxCalories[k] = temp
                            temp = temp2
                            k += 1    
                        else:
                            k += 1
                else:
                    i=3
            i += 1
        Calories = 0
       
       
k = 0
while k < 3 :
    Total += MaxCalories[k]
    k+=1
print(str(Total))


