#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 08:39:44 2018

@author: cristhianmurcia
"""
import datetime


class Contact(object):    
    """
    Representation of a single contact.
    """
    
    def __init__(self, name, lastName, age, phoneNumber, email):            
        """
        Initializes a Contact instance, saves all parameters as attributes
        of the instance.        
        """    
        self.__name = name
        self.__lastName = lastName
        self.__fullName = self.__name + ' ' + self.__lastName
        self.__age = age
        self.__phoneNumbers = {}
        self.__phoneNumbers['Personal'] = phoneNumber
        self.__email = email
        self.__date = str( datetime.datetime.now())
        self.__hide = False
        
    def __str__(self):
        return f"name : {self.__name}, lastName : {self.__lastName}, age : {self.__age}, phoneNumber : {self.__phoneNumbers}, email : {self.__email}, Creation Date : {self.__date}"

    def getName(self):
        """
        Returns the contact's name.
        """
        return self.__name
    
    def getLastName(self):
        """
        Returns the contact's last name.
        """
        return self.__lastName
    
    def getAge(self):
        """
        Returns the contact's last name.
        """
        return self.__age

    def getPhoneNumber(self):
        """
        Returns the contact's phone number.
        """
        return self.__phoneNumbers
    
    def getEmail(self):
        """
        Returns the contact's email.
        """
        return self.__email
    
    def getDate(self):
        """
        Returns the contact's date.
        """
        return self.__date
    
    def getHide(self):
        return self.__hide
    
    def getFullName(self):
        return self.__fullName
    
    def setName(self, name):
        """
        Sets the contact's name.
        """
        self.__name = name
    
    def setLastName(self, lastName):
        """
        Sets the contact's last name.
        """
        self.__lastName = lastName
    
    def setAge(self, age):
        """
        Sets the contact's last name.
        """
        self.__age = age

    def setPhoneNumber(self, phoneNumber, phoneNumberType = 'Personal'):
        """
        Sets the contact's phone number.
        The parameter phoneNumberType is related to their usage (for instance. Home, Office, Personal)
        """        
        self.__phoneNumbers[phoneNumberType] = phoneNumber
    
    def setPhoneNumbers(self, phoneNumbers):
        """
        Replaces the current phoneNumbers dict
        """
        self.__phoneNumbers = phoneNumbers
    
    def setEmail(self, email):
        """
        Sets the contact's email.
        """
        self.__email = email
    
    def setDate(self, date):
        """
        Sets the contact's date.
        """
        self.__date = date
        
    def setHide(self, hide):
        self.__hide = hide
    
    @staticmethod
    def contactAvailableAttributes():
        """
        Returns a list containing the available attributes to be stored in this class.
        """
        return ["name", "lastName", "age", 'phoneNumber', 'email']
        
        
class ContactList(object):
    """
    Representation of a contact list which can store and modify several single contact instances.
    """
    def __init__(self, name):            
        """
        Initializes a Contact List instance.
        
        name : Corresponds to the contact list name. This parameter is useful to write the contact
        list as a file, which can be found in the future.
        
        contactList : Stores several contact instances in a dictionary. The key belongs to the 
        contact full name (Name and Last Name. For instance "Cristhian Murcia") and the value 
        belongs to the contact instance. Using a dictionary reduces the complexity when finding a contact,
        since it works like a hash map O(1)
        
        Contacts are stored in two data structures, a dict to acces them and a list to keep them organized
        
        """    
        self.__name = name
        self.__contactListDict = {}
        self.__contactList = []
        self.__possibleAttributes = Contact.contactAvailableAttributes()
    
    def addContact(self, name, lastName, age, phoneNumber, email):
        """
        Adds a new contact to the contact list.
        """
        newContact = Contact(name, lastName, age, phoneNumber, email)
        self.__contactListDict[newContact.getFullName()] = newContact
        self.__contactList.append(newContact)
        
        #Contacts inside the contact list are always sorted according to thei creation date
        #from the most receantly added to the latest.
        self.__contactList = sorted(self.__contactList, key = lambda x : x.getDate(), reverse = True )
        
    def findContact(self, contactName):
        """
        Finds a contact according to their full name (Name + " " + LastName)
        
        contactName : A string of the type Name LastName (for instance. 'Cristhian Murcia')
        """       
        #Finding contact using a dict is faster than going through a list
        try:
            contact = self.__contactListDict[contactName]
            return contact
        except KeyError:

            return None
            
    def updateContact(self, contactFullName, attribute, value):
        """
        Finds a contact according to their full name (Name + " " + LastName) and updates
        one of its attributes with a new value
        
        contactFullName : Contact to be updated. A string of the type Name LastName (for instance. 'Cristhian Murcia')
        
        attribute : Contact's attribute to be updated. Can be one of the following : name, lastName, phoneNumber and email
        value : new value to be assigned
        """
        #check this
        contact = self.findContact(contactFullName)
        if contact is not None:        
            if attribute in self.__possibleAttributes:
                if attribute == "name":
                    contact.setName(value)
                elif attribute == "lastName":
                    contact.setLastName(value)
                elif attribute == "age":
                    contact.setAge(value)            
                elif attribute == "phoneNumber":
                    contact.setPhoneNumber(value)
                elif attribute == "email":
                    contact.setEmail(value)
                else:
                    print(f"Could not find attribute, try one of the followings : {self.__possibleAttributes}")
        #Updates dictionary key, which might have changed due to a new name or lastName value
        self.updateDict()
    def addAdditionalPhoneNumber(self, contactFullName, phoneNumber, phoneType = "Personal") :
        """
        Finds a contact according to their full name (Name + " " + LastName) and adds an additional phone number.
        """
        contact = self.findContact(contactFullName)
        if contact is not None:  
            phones = contact.getPhoneNumber()
            newPhones = phones.get(phoneType, [])
            newPhones.append(phoneNumber)
            phones[phoneType] = newPhones
            self.__contactListDict.update(phones)
            
    def hideContact(self, contactFullName) :
        """
        Hides an existing contact. If the contact is hidden, it is not shown by the displayContactList function
        """
        contact = self.findContact(contactFullName)
        if contact is not None:
            contact.setHide(True)
            
    def unhideContact(self, contactFullName) :
        """
        Unhides an existing contact, as a result, the contact is shown by the displayContactList function
        """
        contact = self.findContact(contactFullName)
        if contact is not None:
            contact.setHide(False)
            
    def displayContacts(self):
        """
        Displays each of the contacts stored inside the contactList attribute.
        """
        print("")
        strRepresentation = [str(i + 1) + ". " + c.__str__() for i,c in enumerate(self.__contactList) if not c .getHide()]

        for s in strRepresentation:
            print (s)
            print("")
            
    def updateDict(self):
        """
        Updates the __contactListDict attibute with new keys. This function must be executed
        after the user changes a contact name or last name since their keys are name + " " + lastName
        """
        newContactDict = {}
        for c in self.__contactList:
            newKey = c.getName() + " " + c.getLastName()
            newContactDict[newKey] = c
        self.__contactListDict = newContactDict
        
    def getContactList(self):
        return self.__contactList
    
    def setContactList(self, newList):
        self.__contactList = newList
    
    def getName(self):
        return self.__name
    
    
class User(object):        
    """
    Representation of a User. This class directly interacts with the ContactList and Contact classes
    """    
    def __init__(self, name, password): 
        self.__name = name
        self.__password = password
        self.__contactList = None
        self.listAttributes = Contact.contactAvailableAttributes()
    
    def createContactList(self, contactListName):
        self.__contactList = ContactList(contactListName)
        
    def addContact(self):
        attributes = Contact.contactAvailableAttributes()
        print(f"Welcome to the add contacts module to add a new contact please enter the following attributes : {attributes}.")
        name = input("1. Please enter the contact name : ") 
        lastName = input("2. Please enter the contact last name : ")  
        age = input("3. Please enter the contact age : ")  
        phoneNumber = input("4. Please enter the contact phone number : ")  
        email = input("5. Please enter the contact email : ")
        self.__contactList.addContact(name, lastName, age, phoneNumber, email)         
    
    def contactGenerator(self):
        userAnswer = input("To stop adding contacts hit the q key otherwise hit any letter. ")  
        if userAnswer != "q":
            yield self.addContact()
       
    def addContacts(self):
        self.addContact()
        try:
            while True:
                next(self.contactGenerator())
        except StopIteration:
            pass
    
    def updateContact(self):
        print("Currently your list has the following contacts : ")
        self.showContacts()
        contactFullName = input("Please enter the full name of the contact that you want to update in this format 'name' + ' ' + 'lastName' (for example Cristhian Murcia) : ")
        if self.__contactList.findContact(contactFullName) is not None:
            attribute = input(f"Now enter the attribute that you want to update. You can choose one of the following : {self.listAttributes} : ")
            if attribute in   self.listAttributes :
                value = input("Now enter the new value : ")
                self.__contactList.updateContact(contactFullName, attribute, value)
                print("Displaying your list after updating their contact attributes ")               
                self.showContacts()
            else:
                print (f"Attribute {attribute} not in {self.listAttributes}.")
        else : 
            print (f"Contact {contactFullName} not in list.")        
        
    def addAditionalPhoneNumer(self):
        print("Currently your list has the following contacts : ")
        self.showContacts()
        contactFullName = input("Please enter the full name of the contact that you want to update : ")
        if self.__contactList.findContact(contactFullName) is not None:
            phoneType = input("Please enter the type of mobile phone (for instance Personal, Home, Office) : ")
            phoneNumber = input("Please enter the new phone number : ")
            self.__contactList.addAdditionalPhoneNumber(contactFullName, phoneNumber, phoneType)
            print("Displaying the changes that you made.")
            self.showContacts()
        else : 
            print (f"Contact {contactFullName} not in list.")
        
    def hideContact(self):
        print("Currently your list has the following contacts : ")
        self.showContacts()
        fullName = input("To hide a contact please enter its full name in this format 'Name' + ' ' + 'LastName' (for instance. Cristhian Murcia) : ")
        if self.__contactList.findContact(fullName) is not None:
            self.__contactList.hideContact(fullName)
            print("")
            print("Now your list has the following contacts : ")
            self.showContacts()
        else : 
            print (f"Contact {fullName} not in list.")
        
    def unhideContact(self):
        print("Currently your list has the following contacts : ")
        self.showContacts()
        fullName = input("To unhide a contact please enter its full name in this format 'Name' + ' ' + 'LastName' (for instance. Cristhian Murcia) : ")
        if self.__contactList.findContact(fullName) is not None:
            self.__contactList.unhideContact(fullName)
            print("")
            print("Now your list has the following contacts : ")
            self.showContacts()
        else : 
            print (f"Contact {fullName} not in list.")
    
    def showContacts(self):
        self.__contactList.displayContacts()
        
    def sortContacts(self):
        order = input("To sort starting from the most recent date to the oldest date type r otherwise type o : ")
        if order == "r":
            newContactList = sorted(self.__contactList.getContactList(), key = lambda x : x.getDate(), reverse = True )
            self.__contactList.setContactList(newContactList)
            print("Displaying the changes that you made.")
            self.showContacts()
        elif order == "o":
            newContactList = sorted(self.__contactList.getContactList(), key = lambda x : x.getDate(), reverse = False )    
            self.__contactList.setContactList(newContactList)
            print("Displaying the changes that you made.")
            self.showContacts()
        else : 
            print("Option not found")
    
    def getUserName(self):
        return self.__name
        
    def getPassword(self):
        return self.__password
    
    def getContactList(self):
        return self.__contactList        
   