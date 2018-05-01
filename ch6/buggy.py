import random
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
print("what is " + str(number1) + " + " + str(number2) + "?")
answer = input()
if int(answer) == number1 + number2:
    print("Correct!")
else:
    print("Wrong! The answer is " + str(number1 + number2))
