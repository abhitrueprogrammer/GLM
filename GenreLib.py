def genreChooser():
    print("Choose the genere of the game (if you want multiple, seperate each by comma):")
    genreDict = {1: "Action", 2: "Action Adventure", 3: "Adventure", 4: "Role Playing", 5: "Simulation", 6: "Statergy", 7: "Sports", 8: "MMO", 9: "First Person Shooter", 10: "Sandbox"}
    for i in genreDict:
        print(f"{i}. {genreDict[i]}") #printing The genres and its indecies on the screen
    genreLst =[]
    while True:
        try:
            for i in GetGenreNums():
                genreLst.append(genreDict[i])
            print(genreLst)
            break
        except KeyError:    #if the num entered is out of index of the dictionary
            print("Careful, you wanna choose a genre only from the given list. ie, your choices should be from 1-10 not more or less than that: " )
            genreLst.clear()
        except NameError as DuplicateValueError:    #if duplicate values are used.
            print(DuplicateValueError.args)
    return(genreLst)
    
def stringToLst(stringNum):
    numlst = []
    lstStringNum = stringNum.split(",")
    for i in lstStringNum:
        numlst.append(int(i))
    for i in numlst:
        if numlst.count(i) > 1: #if a number is repeated twice.
            raise NameError("DuplicateValueError")
    return numlst

def GetGenreNums():
        while True:
            try:
                numTuple = input()
                GenreNums = stringToLst(numTuple)
                break
            except ValueError:
                print("Oops incorrect number entered/wrong delimiter used. Try again!")
        return GenreNums