hardness = float(input("Enter hardness of steel: "))
carbon = float(input("Enter carbon content of steel: "))
tensile = float(input("Enter tensile strength of steel: "))

if hardness > 50 and carbon < 0.7 and tensile > 5600:
    grade = 10
elif hardness > 50 and carbon < 0.7:
    grade = 9
elif carbon < 0.7 and tensile > 5600:
    grade = 8
elif hardness > 50 and tensile > 5600:
    grade = 7
elif hardness > 50 or carbon < 0.7 or tensile > 5600:
    grade = 6
else:
    grade = 5
print("Grade of the steel:", grade)
