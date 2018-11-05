#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 08:39:44 2018

@author: cristhianmurcia
"""
import os
import pickle
from Classes import User


def printMenu(userName, listName):
    print("")
    print(f"Welcome {userName}! In this application you can perform the following actions on your newly created {listName} contact list: ")
    print("1. Add a new contact to your list.")
    print("2. Sort your list according to the date in which the contacts were added. Either starting from the most recent date or from the oldest date.")
    print("3. Update existing contact.")
    print("4. Hide an existing contact so that it is not shown.")
    print("5. Unhide an existing contact so that it can be displayed.")
    print("6. Display your contact list.")
    print("7. Add an additional telephone number (more than one).")
    print("8. Save your user name and credentials.")
    print("9. Exit the application.")
    

    

def controller(myUser):
    while True:
        printMenu(myUser.getUserName(), myUser.getContactList().getName())
        answer = input("Select one option from the menu, type a number (i.e. 1) : ")
        print("")
        if answer == "1" :
            myUser.addContacts()
            newAnswer = input("To stop experimenting with your list type n, to continue working type any key : ")
            if newAnswer == "n" :
                break
        elif answer == "2":
            myUser.sortContacts()
            newAnswer = input("To stop experimenting with your list type n, to continue working type any key : ")
            if newAnswer == "n" :
                break
        elif answer == "3":
            myUser.updateContact()
            newAnswer = input("To stop experimenting with your list type n, to continue working type any key :")
            if newAnswer == "n" :
                break
        elif answer == "4":
            myUser.hideContact()
            newAnswer = input("To stop experimenting with your list type n, to continue working type any key : ")
            if newAnswer == "n" :
                break
        elif answer == "5" :
            myUser.unhideContact()
            newAnswer = input("To stop experimenting with your list type n, to continue working type any key : ")
            if newAnswer == "n" :
                break
        elif answer == "6":
            myUser.showContacts()
            newAnswer = input("To stop experimenting with your list type n, to continue working type any key : ")
            if newAnswer == "n" :
                break
        
        elif answer == "7":
            myUser.addAditionalPhoneNumer()
            newAnswer = input("To stop experimenting with your list type n, to continue working type any key : ")
            if newAnswer == "n" :
                break
        
        elif answer == "8":
            userFile = open("".join([myUser.getUserName(), myUser.getPassword()]), "wb")
            userFile.write(pickle.dumps( myUser))
            userFile.close()


        elif answer == "9":
            break
        else :
            print("Option not available!!!, please pick a number between 1 and 7 according to the menu.")



def newUser():
    userName = input("To start the contact list application please type your user name : ")
    password = input("Please insert a password consisting of only numbers : ")
    listName = input(f"Welcome {userName}!!!! now please type the name of your contact list : ") 
    myUser = User(userName, password)
    myUser.createContactList(listName)
    controller(myUser)

def loadExistingUser():
    userName = input("Please type your user name : ")
    password = input("Please insert your password : ")
    lookingFor = userName + password   
    files = os.listdir(os.getcwd())
    myUser = None
    if lookingFor in files:
        f2 = open(lookingFor, "rb")
        from_file = f2.read()
        f2.close()
        myUser = pickle.loads(from_file)
        controller(myUser)
    else:
        print(f"User {userName} is not registered or the password is wrong!!")


def initialPrompt():
    print("------------------------------------")
    print("Welcome to the contact list application.")
    while True:
        print("1. Creat a new user.")
        print("2. Load Existing user.")
        print("3. Exit application.")
        selection = input("Please choose one of the following options typing a number : ")
        if selection == "1":
            newUser()
            break
        elif selection == "2":
            loadExistingUser()
        elif selection == "3":
            break
        else:
            print("Choose a correct option")
            
            
