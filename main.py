import SQLib
import backend
SQLib.createTable()

print("Library Management system created by Abhinav Pant, under GNU General Public License.")

# Asking the user to add a game entry if not already added
if SQLib.tableEmpty() == True:
    print("You have not added any entries in the database! Add at least one entry:")
    backend.addEntry()


def showMenuGetInput():
    print("-"*50)
    functionDictionary = {'v': "View the library", 'a': "Add  a new entry", 'd': "Delete a entry",
                   's': "Search for something", 'u': "Update a existing entry", 'q': "quit"}  # dictonary to store the menu entries
    for i in functionDictionary:
        print(i + ". ", functionDictionary[i])
    menuChoice = input("Enter the function you wanna execute: ")
    print("-"*50)
    return menuChoice


userChoice = showMenuGetInput()
def execute_user_choice(userChoice):
    match userChoice:
        case 'v':
            SQLib.show_all()
        case 's':
            backend.search()
        case 'a': 
            backend.addEntry()
        case 'd': 
            backend.DelRec()
        case 'u':
            backend.UpdateRec()
        case '_':
            print("invalid Input")
        
    

while userChoice != 'q':
    execute_user_choice(userChoice)
    userChoice = showMenuGetInput()

SQLib.closeDB()
print("Credits for this programme: Mr. Atul Verma, Codeacademy, Stackoverflow, GeeksforGeeks, Sagnik(for testing)")
