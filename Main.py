import random

attempts = 0
left = int(input("minimal number"))
right = int(input("maximal number"))
print("Hello")
number = random.randint(left,right)
while(True):
    question = input(f"is the number {number} right? [y/h/l]: ")
    attempts += 1
    if question == "h":
        left = number + 1
        print(str(left) + "|" +str(right))
    elif question == "l":
        right = number - 1
        print(str(left) + "|" + str(right))
    else:
        print("yay")
        print(f"attempts: {attempts}")
        break
    number = round((left + right) / 2)
#usrinpt = input(">")