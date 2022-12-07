m = float(input("How much was the meal? "))

n = int(input("What percentage would you like to tip? ").replace("%", ""))

a = n /int(100)

b = m * a

print(b)