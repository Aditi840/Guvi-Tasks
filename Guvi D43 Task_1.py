# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:39:15 2023

@author: Aditi
"""

#Guvi D43 Task_1
#Python login system using file handling.

import re

def register():
    while True:
        username = input("Enter a valid email address: ")
        if re.match(r'^[a-zA-Z0-9._]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$', username):
            break
        else:
            print("Invalid email format.Please try again.")
    while True:
        password = input("Enter a valid password(5-16 characters,with atleast one digit, uppercase letter,lower case letter,and special character): ")
        if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+-=])[a-zA-Z0-9!@#$%^&*()_+-=]{5,16}$', password):
            break
        else:
            print("Invalid password format.Please try again.")
            
    with open("user1_data.txt","a") as f:
        f.write(f"{username},{password}\n")
        
    print("Registeration successful!")
    
def login():
    username = input("Enter a valid username ")
    password = input("Enter a valid password ")
    found = False
    
    with open("user1_data.txt","r") as f:
        for line in f:
            if line.strip() == f"{username},{password}":
                print("Login successful!")
                found = True
                break;
            elif line.startswith(username):
                print("Invalid password! please try again!")
                found = True
                break
            
    if not found:
        
        choice = input("username not found, Do you want to register? (y/n): ")
        if choice == "y":
            register()
        else:
            print("Goodbye!")

def reset_password():
    email = input("Enter a valid email address")
    with open("user1_data.txt","r") as f:
        for line in f:
            user_email,user_password = line.strip().split(",")
            if email==user_email:
                new_password = input("Enter your password(5 < password length > 16), with atleast one special character, one digit,one uppercase,one lowercase character): ")
                if re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+-=])[a-zA-Z0-9!@#$%^&*()_+-=]{5,16}$', new_password):
                    line_to_replace = f"{user_email},{user_password}"
                    new_line = f"{user_email},{new_password}"
                    with open("user1_data.txt","r+") as f:
                        data = f.read()
                        new_data = data.replace(line_to_replace, new_line)
                        f.seek(0)
                        f.write(new_data)
                        f.truncate()
                    print("Password reset successful!")
                else:
                    print("Invalid password!")
                return
    print("Email address not found, or register if you don't have an account.")
    
#main program loop
while True:
    choice = input("Enter 1 to register, 2 to login,3 to reset password.")
    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        reset_password()
    else:
        print("Invalid choice,Please try again.")
                
           
    
       
    
