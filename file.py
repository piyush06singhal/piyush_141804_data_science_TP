import os
def write_file():
    with open('file.xlsx', 'w') as f:
        f.write("\n")
        f.write(',"Hello, World"\n')
write_file()
def read_file():
    with open('./file.xlsx', 'r') as f:
        print(f.read())
read_file()


