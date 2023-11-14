with open('input.txt', 'r') as file:
    for line in file:
        text = line
        
unique = []


for i in range(len(text)):
    if not unique:
        unique.append(text[i])
    
    elif text[i] in unique:
        index = unique.index(text[i])
        if index == 14:
            unique =[]
        else:
            unique = unique[index+1:]
        unique.append(text[i])
    
    else:
        unique.append(text[i])   
    
    if len(unique) == 14:
        print(unique)
        print("First marker after character: " + str(i+1))
        break