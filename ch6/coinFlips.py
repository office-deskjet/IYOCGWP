import random
print("I will lfip a coin 1000 time. Guerss how many times it will come up heads. (press enter to being)")
input()
flips = 0
heads = 0
while flips < 1000:
    if random.randint(0,1) == 1:
        heads = heads + 1
    flips = flips + 1

    if flips == 900:
        print("900 flips and there have been " + str(heads) + " heads.")
    if flips == 100:
        print("At 100 tosses, heads has come up " + str(heads) + " times.")
    if flips == 500:
        print("Half way done, and heads has come up " + str(heads) + " so far.")

print()
print("Out of 100 coin tosses, heads came up " + str(heads) + " times.")
print("were you close?")
