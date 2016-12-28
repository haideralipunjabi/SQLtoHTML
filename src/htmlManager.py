import markup
import src.fileManager as fileManager
import os
class htmlManager:
    def __init__(self):
        self.page = markup.page()
        self.page.init()
        self.page.table(class_="sortable")

    def addHeader(self, columns):
        self.page.tr()
        print(len(columns))
        for column in columns:
            self.page.th(column)
        self.page.tr.close()

    def addData(self, rows):
        for row in rows:
            self.page.tr()
            for cell in row:
                self.page.td(cell)
            self.page.tr.close()
        self.page.table.close()
    def print(self, database):
        file = open(str(database).rstrip(".db") + ".html","w+")
        file.write(str(self.page))
        file.close()

