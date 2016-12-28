import sqlite3

class databaseManager:



    def __init__(self, database):
        self.database = database
        self.connection = sqlite3.connect(self.database)
        self.cursor = self.connection.cursor()

    def getTables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return (self.cursor.fetchall())

    def getColumnNames(self, table):
        self.cursor.execute("PRAGMA table_info(%s)"%(table))
        columns = self.cursor.fetchall()
        columnNames = []
        for column in columns:
            columnNames.append(column[1])
        return columnNames

    def getRows(self,table):
        self.cursor.execute("SELECT * from %s"%(table))
        return self.cursor.fetchall()
