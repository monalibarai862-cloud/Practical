name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

total = 0
print("Enter monthly purchase amounts:")

for i in range(12):
    amount = float(input("Amount: "))
    total = total + amount
print("\nVendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase:", total)
