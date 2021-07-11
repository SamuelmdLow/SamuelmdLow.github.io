'''
TITLE:  Horrible Text Based Blogging!
AUTHOR: Samuel Low
DATE CREATED:   10 July 2021
'''

# --- Setup ---
import sqlite3
import pathlib

blog = "blog.db"

FIRST_RUN   =   True
if (pathlib.Path.cwd() / blog).exists():
    FIRST_RUN   =   False

connection = sqlite3.connect(blog)
cursor = connection.cursor()

# --- Functions ---

def setUpDB():
    global connection, cursor

    cursor.execute('''
        CREATE TABLE 
            posts(
                id INTEGER PRIMARY KEY,
                time INTEGER,
                entry TEXT
            )
    ;''')

    connection.commit()

    print("Created blog database file!")

def menu():
    print('''
    Chose:
        1. Add a post
        2. Edit a post
        3. Delete a post
        4. End 
    ''')
    selection = int(input(">"))

    return selection

def runFunction(selection):
    global finished

    if selection == 1:
        addPost()
    elif selection == 2:
        editPost()
    elif selection == 3:
        deletePost()
    else:
        finished = True

def addPost():
    pass

def editPost():
    pass

def deletePost():
    pass


# --- Main Program Code ---

if FIRST_RUN == True:
    setUpDB()

finished = False

print("Welcome to Your Horrible Text Based Blogging Program!")

while not finished:
    selection = menu()
    runFunction(selection)