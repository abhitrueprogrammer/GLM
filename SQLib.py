import sqlite3

conn = sqlite3.connect('gameList.db')
cursor = conn.cursor()


def createTable():
    cursor.execute("""CREATE TABLE IF NOT EXISTS gameList
    (
    NAME TEXT,
    PLATFORM TEXT,
    GENRE TEXT,
    DEV TEXT,
    USERSCORE INTEGER
    )
    """)


def addVals(gameEntry):
    print(gameEntry)
    cursor.execute(f"INSERT INTO gameList VALUES {gameEntry}")
    conn.commit()


def tableEmpty():
    cursor.execute("""SELECT count(*) from gameList""")
    if cursor.fetchall() == [(0,)]:
        return True
    else:
        return False


def show_all():
    cursor.execute("SELECT rowid, * FROM gameList")
    data = cursor.fetchall()
    print("RowID", "NAME" + " "*28, "PLATFORM" + " " * 13, "GENRE" + " " *
          45 + "DEV" + " " * 19, "USERSCORE", end="\n" + "-" * 140 + "\n")
    for item in data:
        for i in range(6):  # look out a way to calculate max spaces by columms
            noOfSpaces = 0
            if i == 0:
                noOfSpaces = 4
            if i == 1:
                noOfSpaces = 32 - len(item[i])
            if i == 2:
                noOfSpaces = 20 - len(item[i])
            if i == 3:
                noOfSpaces = 50 - len(item[i])
            if i == 4:
                noOfSpaces = 22 - len(item[i])
            print(item[i], noOfSpaces * " ", end="")

        print()


def delete_record(rowID):
    cursor.execute(f"DELETE FROM gameList WHERE rowid = {rowID}")
    conn.commit()
    cursor.execute(f"SELECT COUNT(*) FROM gameList WHERE rowid = {rowID}")
    if cursor.fetchall() == [(0,)]:
        return True
    else:
        return False


def updateRec(rowID, updatedInfo):
    columnList = ("NAME", "PLATFORM", "GENRE", "DEV",
                  "USERSCORE")  # make this global beech
    cursor.execute(
        f"UPDATE gameList SET {columnList} = {updatedInfo} WHERE rowid = {rowID}")
    conn.commit()


def closeDB():
    cursor.close()
    conn.close()


def findRec(searchTerm, catagory):
    catagory = catagory.upper()
    cursor.execute(
        f"SELECT * FROM gamelist WHERE {catagory} like '%{searchTerm}%'")
    return cursor.fetchall()


def check_if_rowID_exists(rowID):
    cursor.execute("""SELECT rowid from gameList""")
    data = cursor.fetchall()
    for tuple_of_row_ids in data:
        if rowID in tuple_of_row_ids:
            return True
    return False
