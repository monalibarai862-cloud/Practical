voltage = float(input("Enter voltage (V): "))
resistance = float(input("Enter resistance (Ω): "))

current = voltage / resistance
print("Current (I) = {:.2f} A".format(current))
if current < 0.5:
    print("Low current")
elif 0.5 <= current <= 2:
    print("Normal current")
else:
    print("High current")
