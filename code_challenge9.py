# code_challenge9.py
# countdown timer simulator with delay to act as a real countdown

import time

print("" COUNTDOWN TIMER SIMULATOR")

start = eval(input("Enter the starting number for countdown: "))

print("\nCountdown started:")

for cd in range(start, 0, -1):
    print(cd)
    time.sleep(1)
print("Liftoff! ")