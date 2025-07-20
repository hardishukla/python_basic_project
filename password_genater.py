#password genrator
import random
import string
length=int(input("enter length of password : "))#user input
character=string.ascii_letters + string.digits + string.punctuation#digits,punctuation,and alphabets
password="".join(random.choice(character) for x in range(length))
print(password)
