source = input("Enter source python file: ")
destination = input("Enter destination file: ")

f1 = open(source, "r")
f2 = open(destination, "w")

for line in f1:
    if not line.strip().startswith("#"):   # ignore comments
        f2.write(line)

f1.close()
f2.close()

print("Content copied without comments.")