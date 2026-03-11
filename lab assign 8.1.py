source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

f1 = open(source, "r")
data = f1.read()

f2 = open(destination, "w")
f2.write(data.upper())

f1.close()
f2.close()

print("File copied successfully in uppercase.")