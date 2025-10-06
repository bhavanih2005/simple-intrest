# Simple and Compound Interest Calculator
P = float(input("Enter the principal amount: "))
R = float(input("Enter the rate of interest: "))
T = float(input("Enter the time (in years): "))
SI = (P * R * T) / 100
print("Simple Interest: ₹", round(SI, 2))
A = P * (1 + R / 100) ** T
