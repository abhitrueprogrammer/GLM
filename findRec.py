import sqlite3
conn = sqlite3.connect('gameList.db')
cursor = conn.cursor()

def findRec(searchTerm,catagory):
    catagory = catagory.upper()
    cursor.execute(f"SELECT * FROM gamelist WHERE {catagory} like '%{searchTerm}%'")
    return cursor.fetchall()