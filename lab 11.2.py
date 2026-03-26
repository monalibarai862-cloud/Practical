import matplotlib.pyplot as plt

companies = ["Microsoft", "Google", "Amazon", "IBM", "Amdocs"]
recruitments = [120, 150, 180, 90, 110]

plt.bar(companies, recruitments)
plt.title("Recruitments in Companies")
plt.xlabel("Companies")
plt.ylabel("Number of Recruitments")
plt.show()

plt.pie(recruitments, labels=companies, autopct="%1.1f%%")
plt.title("Recruitment Distribution")
plt.show()

plt.pie(recruitments, labels=companies, autopct="%1.1f%%",
        explode=[0, 0.1, 0, 0, 0])
plt.title("Customized Pie Chart")
plt.show()

plt.pie(recruitments, labels=companies, autopct="%1.1f%%")
centre_circle = plt.Circle((0, 0), 0.5, fc='white')
plt.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

names = ["IBM", "Amdocs"]
values = [90, 110]

plt.bar(names, values)
plt.title("IBM vs Amdocs Recruitment")
plt.show()