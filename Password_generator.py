import string
import random

lenght=int(input("Enter your password lenght: "))
print(''' Choose characters set for password from these: 
           1. Digits
           2. Letters
           3. Special Characers
           4. Exit!''')
characterList= ""
while(True):
    choice=int(input("Pick a Number "))
    if(choice == 1):
        characterList += string.ascii_letters
    elif(choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("please pick a valid option!")
password = []
for i in range(lenght):
    randomchar = random.choice(characterList)
    password.append(randomchar)
print("The random password is " + "".join(password))