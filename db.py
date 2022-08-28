#coding:utf-8
import sqlite3 as lit
class GameWord:
    def __init__(self):
        self.__auth = "Kevin Thierry"

    def connectToDatabase(self):
        return lit.connect('game.db')

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
            (1, 'VACHE'),
            (2, 'LAPIN'),
            (3, 'BREBIS'),
            (4, 'ANE'),
            (5, 'CANARD'),
            (6, 'CANE'),
            (7, 'BOEUF'),
            (8, 'COQ'),
            (9, 'POULE'),
            (10, 'POUSSIN'),
            (11, 'ANESSE'),
            (12, 'BAUDET'),
            (13, 'CHEVAL'),
            (14, 'JUMENT'),
            (15, 'CHEVRE'),
            (16, 'BOUC'),
            (17, 'COCHON'),
            (18, 'VERRAT'),
            (19, 'TRUIE'),
            (20, 'DINDON'),
            (21, 'DINDE'),
            (22, 'LAPINE'),
            (23, 'MOUTON'),
            (24, 'BELIER'),
            (25, 'TAREAU')
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

"""
game = GameWord()
game.connectToDatabase()
game.createTable()
game.insertData()
print(game.getData())
"""
