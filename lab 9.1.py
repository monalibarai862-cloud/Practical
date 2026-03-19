class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def get_data(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.salary = float(input("Enter salary: "))
        self.address = input("Enter address: ")

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)
class Manager(Employee):
    def __init__(self):
        super().__init__("", 0, 0, "")

managers = []

for i in range(2):   # change to 10 if needed
    print(f"\nEnter details of Manager {i+1}")
    m = Manager()
    m.get_data()
    managers.append(m)

print("\n--- Manager Details ---")
for m in managers:
    m.display()