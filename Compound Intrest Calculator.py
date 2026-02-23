

from sqlite3 import Time


principle = 0

rate = 0

time = 0

while principle <= 0:
    principle = float(input("Enter the princple amount: "))
    if principle <= 0:
        print("Principle cant be less than or equal to zero")

while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Interest rate cant be less than or equal to zero")

while time <= 0:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time cant be less than or equal to zero")

        print(principle)
        print(rate)
        print(time)

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
