#coding:utf-8
import sqlite3 as lit
class GameWord:
    def __init__(self):
        self.__auth = "Kevin Thierry"

    def connectToDatabase(self):
        return lit.connect('wordGame.db')

    def createTable(self):
        try:
            db = self.connectToDatabase()
            cur = db.cursor()
            tablequery = "CREATE TABLE words (id INT, word TEXT)"

            cur.execute(tablequery)
            print("Table Created Succesfully")

        except lit.Error as e:
            print("Unable To Create Table")

    def insertData(self):
        mot = (
            (1, 'CACHALOT'),
            (2, 'ORQUE'),
            (3, 'MOINEAU'),
            (4, 'LIONCEAU'),
         )
        db = self.connectToDatabase()
        with db:
            cur = db.cursor()
            cur.executemany('INSERT INTO words VALUES (?,?)', mot)
            print("Data Inserted Successfully")

    def getData(self):
        db = self.connectToDatabase()
        with db:
            cur = db.cursor()
            selectquery = "SELECT word FROM words"
            cur.execute(selectquery)
            liste_mots =  []
            newMot = []
            rows = cur.fetchall()

            for data in rows:
                liste_mots.append(data)
            for i in liste_mots:
                i = list(i)
                y = i[0]
                newMot.append(y)
            return newMot

    def updateData(self):
        db = self.connectToDatabase()
        with db:
            newname = "updatedword"
            user_id = 1

            cur = db.cursor()
            cur.execute('UPDATE words SET name = ? WHERE id = ?', (newname, user_id))
            db.commit()
            print("Data Updated Successfully")

    def deleteData(self):
        db = self.connectToDatabase()
        with db:
            user_id = 1
            cur = db.cursor()
            cur.execute('DELETE FROM words WHERE id = ?  ', (user_id,) )
            db.commit()
            print("Data Deleted Successfully")
"""
game = GameWord()
game.connectToDatabase()
game.createTable()
game.insertData()
print(game.getData())
"""