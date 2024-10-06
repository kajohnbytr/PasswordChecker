from random import *
import os
u_pwd = input("Enter a password: ")
pwd =  [ 
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
    '0', '1', '2'
]

pw = ""
while(pw!=u_pwd):
    print("new Pass")
    pw = ""
    for letter in range(len(u_pwd)):
        guess_pwd = pwd[randint(0,23)]  
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("Cracking Password... Please wait. ")
        os.system("cls")
print("Your Password is : ", pw)
