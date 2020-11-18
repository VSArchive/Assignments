a = int(input("Enter the first term : "))
b = int(input("Enter the second term : "))


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)


def lcm(a, b):
    return (a * b) / gcd(a, b)


print('GCD is : ', gcd(a, b))
print("LCM is : ", lcm(a, b))
