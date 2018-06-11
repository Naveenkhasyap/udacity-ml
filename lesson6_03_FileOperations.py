#writing to a file
f = open('my_file.txt', 'w')
f.write("Hello there!")
f.close()


#reading a file
f = open('my_file.txt', 'r')
file_data = f.read()
f.close()


#too many handles
files = []
for i in range(10000):
    files.append(open('my_file.txt', 'r'))
    print(i)

#with keyword to read file
with open('my_file.txt', 'r') as f:
    file_data = f.read()