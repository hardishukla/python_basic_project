#count down timer
import time
user=int(input("Enter starting time: "))
for x in range(1,user+1):
    time.sleep(1)
    print(user)
    user=user-1

print("Time is over!!!!")
