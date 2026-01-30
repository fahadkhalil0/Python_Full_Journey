# File Handling In python

# Read a file
open = open("myfile.txt", "r")
read = open.read()
print(read)
open.close()

# write from a file

name = "Fahad"
File = open("myfile.txt", "w")
w = File.write(name)
# print(w)
File.close()


# Readlines function in FIle I/O

# first create a file then read the lines

File = open("file.txt", "w")
W = File.write("Hello, World!\n")
W = File.write("Welcome to the file I/O tutorial.\n")
File.close()


File = open("file.txt", "r")
# w = File.read()
Read1 = File.readline()
Read2 = File.readline()

print(Read1)
print(Read2)
File.close()
print(Read3)


# Appending a data in the file

App = open("file.txt", "a")
A = App.write("Twinkle twinkle little star\n")
# print(A)
App.close()


# read a file in binary mode
File = open("file.txt", "rb")
Content = File.read()
print(Content)
File.close()


# read a file in txt mode
File = open("file.txt", "txt")
Content = File.read()
print(Content)
File.close()

