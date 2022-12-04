import random
import sys
num = random.randint(1, 100)
print(num)
shots = 0
highs = [100]
lows = [1]
while True:
    x = (input("Is it right? "))

    if x == "high":
        shots += 1
        highs.append(num)
        num = random.randint(lows[-1], highs[-1])
        print(num)
    elif x == "low":
        shots += 1
        lows.append(num)
        num = random.randint(lows[-1], highs[-1])
        print(num)
    elif x == "right":
        print(f"It took me {shots} shots")
        sys.exit()
    else:
        print("WRONG VALUE!")
