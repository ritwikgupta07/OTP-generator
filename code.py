import numpy as np

# Enter a phone number (10 digit)
i = int(input())

# Enter the number of digits of otp you want to generate
x = int(input())
x = 10-x
a = i // (10**x)
otp = 0

# Generation of otp
while a>=1:
    l = np.random.randint(a+x)
    otp = (otp*10)+(l % 10)
    a = a/10

# output
print(otp)
