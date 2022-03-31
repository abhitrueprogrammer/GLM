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
    max_spaces = {0: 5, 1: 4, 2: 8, 3: 5, 4: 4, 5: 9}
    for item in data:
        for i in range(len(item)):
            if len(str(item[i])) > max_spaces[i]:
                max_spaces[i] = len(str(item[i]))
    Header = ["RowID", "NAME", "PLATFORM", "GENRE", "DEV", "USERSCORE"]
    for i in range(len(Header)):
        spaces = (max_spaces[i]+1) - len(str(Header[i]))
        print(str(Header[i]) + spaces * " "+" ", end="")
    print()
    for item in data:
        for i in range(len(item)):
            spaces = (max_spaces[i]+1) - len(str(item[i]))
            print(str(item[i]) + spaces * " "+" ", end="")
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
