with open('input.txt', 'r') as file:
    lines = file.readlines()

#  empty list to store file paths and sizes, 
files = []
cwd = ['']


for line in lines:
    command = line.strip()
    if command.startswith("$"):             # Check if we are doing a cd command
        if command.split(" ")[1] == "cd":
            if command.split(" ")[2] == "/":
                cwd = cwd[:1]
            elif command.split(" ")[2] == "..":
                cwd.pop()
            else:
                cwd.append(command.split(" ")[2])
    elif not command.startswith("dir"):
        path = '%s/%s' % ('/'.join(cwd), command.split(" ")[1]) # Construct the full path by joining the current working directory and the specified file or directory
        
        files.append((path, int(command.split(" ")[0])))     # Add the path and its size to the list of files


size = {}

for path, sizes in files:
    names = path.split("/")[:-1]                # Split the path into individual directory names
    for i in range(len(names)):
        name = '/'.join(names[:i + 1])
        size[name] = size.get(name, 0) + sizes

# Print the sum of sizes for directories with sizes less than or equal to 100000
print(sum(x for x in size.values() if x <= 100000))

# Calculate the required size to reach a total of 30000000 and find the smallest directory that meets the requirement
need = 30000000 - (70000000 - size[''])
print(min(x for x in size.values() if x >= need))
