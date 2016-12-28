import src.fileManager as fileManager
import src.databaseManager
import src.htmlManager

html = src.htmlManager.htmlManager()
def chooseDatabase():  # Function to get user input to choose database

    databases = fileManager.getDatabases()
    for file in databases:
        print("[" + str(databases.index(file)) + "] " + file)
    user_input_chooseDatabase = input('Enter database to use: ')
    if int(user_input_chooseDatabase) < len(databases):
        database = src.databaseManager.databaseManager(databases[int(user_input_chooseDatabase)])
        return database
    else:
        print("There was an error processing your input. Input again")
        chooseDatabase()





def chooseTable(database):
    tables = database.getTables()
    modTables = []
    for table in tables:
        modTable = str(str(table).rstrip("',)")).lstrip("('")
        print("[" + str(tables.index(table)) + "] " + modTable)
        modTables.append(modTable)
    user_input_chooseTable = input('Enter table to use: ')
    if int(user_input_chooseTable) < len(modTables):
        table = tables[int(user_input_chooseTable)]
        return table
    else:
        print("There was an error processing your input. Input again")
        chooseTable(database)

def addColumns(database, table):
    html.addHeader(database.getColumnNames(table))
    print(str(database.getColumnNames(table)))

def addRows(database, table):
    html.addData(database.getRows(table))



chosenDatabase = chooseDatabase()
chosenTable = chooseTable(chosenDatabase)[0]
addColumns(chosenDatabase,chosenTable)
addRows(chosenDatabase,chosenTable)
html.print(chosenDatabase.database)




