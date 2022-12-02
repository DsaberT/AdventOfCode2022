file = open('Strategy.txt', 'r')
Lines = file.readlines()

points = 0

#------------------- Part 1 --------------------------
"""
for Line in Lines:
    Lina = Line.rstrip()
    Method = str(Lina[0])+str(Lina[2]) #Add both to make cases
    if Method == "AX":
        points += (1+3)
    elif Method == "AY":
        points += (2+6)
    elif Method == "AZ":
        points += (3)
    elif Method == "BX":
        points += (1)
    elif Method == "BY":
        points += (2+3)
    elif Method == "BZ":
        points += (3+6)
    elif Method == "CX":
        points += (1+6)
    elif Method == "CY":
        points += (2)
    elif Method == "CZ":
        points += (3+3)
print(str(points))
"""

#--------------------Part 2 ------------------------
for Line in Lines:
    Lina = Line.rstrip()
    Method = str(Lina[0])+str(Lina[2]) #Add both to make cases
    if Method == "AX":
        points += (3+0)
    elif Method == "AY":
        points += (1+3)
    elif Method == "AZ":
        points += (2+6)
    elif Method == "BX":
        points += (1+0)
    elif Method == "BY":
        points += (2+3)
    elif Method == "BZ":
        points += (3+6)
    elif Method == "CX":
        points += (2+0)
    elif Method == "CY":
        points += (3+3)
    elif Method == "CZ":
        points += (1+6)
print(str(points))