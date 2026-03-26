import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

facecream = [2500, 2630, 2140, 3400, 3600, 2760]
facewash = [1500, 1200, 1340, 1130, 1740, 1550]
toothpaste = [5200, 5100, 4550, 5870, 6000, 5250]

total_profit = []
for i in range(len(months)):
    total = facecream[i] + facewash[i] + toothpaste[i]
    total_profit.append(total)

plt.plot(months, total_profit)
plt.title("Total Profit per Month")
plt.xlabel("Months")
plt.ylabel("Profit")
plt.show()

plt.plot(months, facecream, label="Face Cream")
plt.plot(months, facewash, label="Face Wash")
plt.plot(months, toothpaste, label="Toothpaste")
plt.legend()
plt.title("Sales of All Products")
plt.show()

x = range(len(months))
plt.bar(x, facecream, width=0.4, label="Face Cream")
plt.bar([i + 0.4 for i in x], facewash, width=0.4, label="Face Wash")
plt.xticks([i + 0.2 for i in x], months)
plt.legend()
plt.title("Face Cream & Face Wash Sales")
plt.show()

total_sales = [
    sum(facecream),
    sum(facewash),
    sum(toothpaste)
]

labels = ["Face Cream", "Face Wash", "Toothpaste"]

plt.pie(total_sales, labels=labels, autopct="%1.1f%%")
plt.title("Yearly Sales Distribution")
plt.show()