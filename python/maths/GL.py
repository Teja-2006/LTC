i = input("Enter two numbers: ")
[a, b] = i.split(" ")
a = int(a)  # Convert input to integers
b = int(b)  # Convert input to integers

# GCD
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

GCD = gcd(a, b)  # Call the gcd function and store the result
LCM = (a * b) // GCD  # Calculate LCM using the correct GCD

print(f"GCD: {GCD} \nLCM: {LCM}")
