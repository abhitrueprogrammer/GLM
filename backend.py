import GenreLib
import SQLib


def GetIntFromUser():
    '''Gets a integer from user and checks for its validity
    Returns: int; Number input by the user '''
    num = ""
    while type(num) is not int:
        try:
            num = int(input())
        except ValueError:
            print("Input numerical value only!")
    return num


def GetRating():
    '''Gets a rating from the user and ensures the rating is a number between 1 to 5
    return: int; user rating.'''
    print("Enter your score for this game out of 5: ", end="")
    rating = 0
    while True:
        try:
            rating = int(input())
            if rating >= 0 and rating <= 5:
                break
            else:
                print("Make sure to rate the game out of 5 only! Even if its the best or worst",
                      "\ntry again!", end=': ')
        except ValueError:
            print("Pass only integers!: ", end='')
    return rating


def getInputForGameEntry():
    '''Asks users for the name, platform, genre, Developer/Publisher and Userscore of the game and adds them to a tuple.
    Return value: Tuple; name, platform, developer and userscore'''
    # asking for values from the user              #add a way to cancel entry midway
    name = input("Enter the name of the game: ").title()
    platform = input("Enter the platform that the game can be played on: ")
    genre = GenreLib.genreChooser()
    DeveloperOrPublisher = input(
        "Enter the Developer or publisher of the Game: ")
    UserScore = GetRating()
    # Adding all the required values to a tuple.
    gameEntry = (name, platform, str(genre), DeveloperOrPublisher, UserScore)
    return gameEntry
# -----------------------------------------x--------------------------------------------------


def addEntry():
    '''Asks user for game entries using a function and adds those values to Database'''
    gameEntry = getInputForGameEntry()
    SQLib.addVals(gameEntry)


def UpdateRec():
    '''Updates a entry in Database, asking user for rowID and details of new entry'''
    SQLib.show_all()
    print("Input the RowID of the thing you want to update")
    rowIDToBeUpdated = GetIntFromUser()
    updatedInfo = getInputForGameEntry()
    SQLib.updateRec(rowIDToBeUpdated, updatedInfo)
    print("Record Successfully updated!")


def DelRec():
    '''Deletes a record using rowID input by the user'''
    SQLib.show_all()
    print("Enter the row ID of the game you want to delete: ", end="")
    rowIDToBeDeleted = GetIntFromUser()
    while not(SQLib.check_if_rowID_exists(rowIDToBeDeleted)):
        print("Given row ID does not exists, please check your input and try again: ", end="")
        rowIDToBeDeleted = GetIntFromUser()
    answer = ""
    print(
        f"Are you sure, you want to delete entry number {rowIDToBeDeleted} (y/n):", end="\n")
    # Very important! You learnt how to implement a function that requires a correct input. First take the input, make sure its correct; then implement it.
    while answer.lower() != "y" and answer.lower() != "n":
        answer = input()
        if answer != 'y' and answer != 'n':
            print("Choose answer as either 'y' or 'n' only! >->. Try again: ", end="")
    if answer.lower() == 'y':
        deleteSucessfull = SQLib.delete_record(rowIDToBeDeleted)
        if deleteSucessfull:
            print("Hai! Record deleted successfully")
        else:
            print("Error! You provided a option that is out of the range of the records. The operation will now be aborted.")
    elif answer.lower() == 'n':
        print("Sokka")


def search():
    '''Searchs for a entry by column'''
    print("Select the catagory you want to search by:")
    # printing menu
    CatagoryDict = {1: "Name", 2: "Platform", 3: "GENRE",
                    4: "DEV", 5: "USERSCORE"}  # make this global beech
    for i in CatagoryDict:
        print(f"{i}. {CatagoryDict[i]}")

    # taking input
    Selection = GetIntFromUser()
    # getting output
    catagory = CatagoryDict[Selection]
    # searching
    searchTerm = input("Enter the search term:")
    Results = SQLib.findRec(searchTerm, catagory)
    print("The matching results are:")
    for i in range(len(Results)):
        print(i+1, ".", Results[i])
