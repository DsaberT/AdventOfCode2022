######################  Part 2  ######################

def counter(i,j):
    left, right, up, down = 0, 0, 0, 0
    for k in range(i -1 , -1, -1):
        if matrix[k][j] < matrix[i][j]:                             #All trees we can see to the left
            left += 1
        else:
            left += 1
            break
    for k in range(j -1, -1, -1):
        if matrix[i][k] < matrix[i][j]:                             #All trees we can see up
            up += 1
        else:
            up += 1
            break
    for k in range(i +1 , len(matrix)):                             #All trees we can see to the right
        if matrix[k][j] < matrix[i][j]:
            right += 1
        else:
            right += 1
            break
    for k in range(j +1 , len(matrix)):                             #All trees we can see down
        if matrix[i][k] < matrix[i][j]:
            down += 1
        else:
            down += 1
            break
    return (int(left * right * up * down ))

######################  Part 2  ######################



with open('input.txt', 'r') as file:
    lines = file.readlines()
    
matrix = []
#Here we create out 99x99 matrix of all the numbers
for line in lines:
    line = line.strip()
    row = []
    for i in range(len(line)):
        row.append(line[i])
    matrix.append(row)


#we add all the boarders so that we count them as visable trees.
visable = int(len(matrix))*4 - 4
hidden = 0

scenic_value = 0
# Iterate through the inner elements (excluding the border))
for i in range(1, len(matrix) - 1):
    for j in range(1, len(matrix[0]) - 1):
        scenic = counter(i,j)
        if all( matrix[i][k] < matrix[i][j] for k in range(0,j)) or all( matrix[i][k] < matrix[i][j] for k in range(j+1,len(matrix))):          #For Row
            visable += 1
        elif all( matrix[k][j] < matrix[i][j] for k in range(0,i)) or all( matrix[k][j] < matrix[i][j] for k in range(i+1,len(matrix))):        #For Coloumn
             visable += 1
        else:
            hidden += 1

        if scenic_value < scenic:
            scenic_value = scenic
            
print("Hidden trees: " + str(hidden) + " Visable Trees: " + str(visable) + " The best scenic value is: " + str(scenic_value))