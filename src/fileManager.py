from os import listdir
from os.path import isfile, join, dirname, abspath

BASE_DIR = dirname(dirname(abspath(__file__)))
def getDatabases():     #Returns databases present in root directory
    databases = []
    for f in listdir(BASE_DIR):
        if(isfile(f) and f.endswith(".db")):
            databases.append(f)

    return databases

def isFile(f):
        if(isfile(f)):
            return True
        else:
            return False

