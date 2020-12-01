#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:03:30 2020

@author: juan
"""

#Declare a Dictionary--------------------------
#The Key is "key":
#The element is "key":"element"
dict={"Name":"Juan","Edad":"19","Licenciatura":"Ciencias de la Computación"}


#We acces the data with the key.
print("dict['Name']:",dict["Name"])
print("dict['Edad']",dict["Edad"])
print("dict['Licenciatura']",dict["Licenciatura"])

print("Original--------------------------")
print(dict)

#-------------------------------------------------------------------------
#Remove entry with it's key.----------------------------------
#del dict["Name"]

#Since we deleted the element in "dict", if we try to print it it throws an error. 
#print("dict['Name']:",dict["Name"])

#Empty the dictionary----------------------------------------
#dict.clear()

#Remove the hole dictionary--------------------------------------------
#del dict
#-------------------------------------------------------------

#Updating the Dictionary-------------------------------------
#Updtin something that already exists in the dictionary with its key.
dict["Edad"]="20"
#Adding a new element with its key
dict["School"]="UNAM"
print("Antes de modificar----------------------------")
print(dict)



