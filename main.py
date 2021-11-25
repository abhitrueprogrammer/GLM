import os
import sqlite3
from sqlite3.dbapi2 import SQLITE_SELECT
from sys import platform
from types import resolve_bases
import GenreLib

import SQLib
SQLib.createTable()
def GetIntFromUser():
    num = ""
    while type(num) is not int:
        try:
            num = int(input())
        except ValueError:
            print("Input numerical value only!")
    return num
def getInputForGameEntry():
    name = input("Enter the name of the game: ").title() #Add a sorting system #add a way to cancel entry midway
    platform = input("Enter the platform that the game can be played on: ")#add a system to only show games from certain platforms
    genre = GenreLib.genreChooser() #add a system to show games from specific genres.
    DeveloperOrPublisher = input("Enter the Developer or publisher of the Game: ")
    UserScore = GetRating()
    gameEntry = (name, platform, str(genre), DeveloperOrPublisher, UserScore)
    return gameEntry
def addEntry():

        # GL.write({name : GameEntry}, end = "\n")
        gameEntry = getInputForGameEntry()
        SQLib.addVals(gameEntry)

def GetRating():
    print("Enter your score for this game out of 5: ", end = "")
    rating = 0
    while True:
        try:
            rating = int(input())
            if rating >= 0 and rating <= 5:
                break
            else:
                print("Make sure to rate the game out of 5 only! Even if its the best or worst", "\ntry again!", end= ': ')
        except ValueError:
            print("Pass only integers!: ", end = '')
    return rating
def UpdateRec():
    SQLib.show_all()
    print("Input the RowID of the thing you want to update")
    rowIDToBeUpdated = GetIntFromUser()
    updatedInfo = getInputForGameEntry()
    SQLib.updateRec(rowIDToBeUpdated, updatedInfo)
    print("Record Successfully updated!")

def DelRec():  
    SQLib.show_all()
    print("Enter the rowid of the game you want to delete: ", sep="")
    rowIDToBeDeleted = GetIntFromUser() #add a way to detect values out of range
    answer = ""
    print(f"Are you sure, you want to delete entry number {rowIDToBeDeleted} (y/n):", end= "\n") 
    while answer.lower() != "y" and answer.lower() != "n": #Very important! You learnt how to implement a function that requires a correct input. First take the input, make sure its correct; then implement it.
        answer = input()
        if answer != 'y' and answer != 'n':
            print("Choose answer as either 'y' or 'n' only! >->. Try again: ", end= "")
    if answer.lower() == 'y':
        deleteSucessfull = SQLib.delete_record(rowIDToBeDeleted)
        if deleteSucessfull:
            print("Hai! Record deleted successfully")
        else:
            print("Error! You provided a option that is out of the range of the records. The operation will now be aborted.")
    elif answer.lower() == 'n':
        print("Sokka")
def search():
        print("Select the catagory you want to search by:")
        #printing menu
        CatagoryDict = {1:"Name", 2: "Platform", 3: "GENRE", 4: "DEV", 5: "USERSCORE"} #make this global beech
        for i in CatagoryDict:
            print(f"{i}. {CatagoryDict[i]}")
        
        #taking input
        Selection = GetIntFromUser()
        #getting output
        catagory = CatagoryDict[Selection]
        #searching
        searchTerm = input("Enter the search term:")
        Results = SQLib.findRec(searchTerm,catagory)
        print("The matching results are:")
        for i in range(len(Results)):
            print(i+1,".", Results[i])
print("Library Management system created by Abhinav Pant, under GNU General Public License.")

# Asking the user to add a game entry if not already added 
if SQLib.tableEmpty() == True:
    print("You have not added any entries in the database! Add at least one entry:")
    addEntry()

def showMenuGetInput():
    print("-"*50)
    fuctionDict = {'v':"View the library", 'a': "Add  a new entry", 'd':"Delete a entry", 's': "Search for something", 'u': "Update a existing entry", 'q': "quit"} #dictonary to store the menu entries
    for i in fuctionDict:
        print(i + ". ", fuctionDict[i])
    menuChoice = input("Enter the fuction you wanna execute: ")
    print("-"*50)
    return menuChoice
userChoice = showMenuGetInput()

while userChoice != 'q':
    if userChoice == 'v':
        SQLib.show_all()
    elif userChoice == 's':
        search()
    elif userChoice == 'a':
        addEntry()
    elif userChoice == 'd':
        DelRec()
    elif userChoice == 'u':
        UpdateRec()
    else:
        print("Invalid Input")
    userChoice = showMenuGetInput()

SQLib.closeDB()
print("Credits for this programme: Mr. Atul Verma, Codeacademy, Stackoverflow, GeeksforGeeks")