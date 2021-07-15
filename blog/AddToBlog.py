'''
TITLE:  Horrible Text Based Blogging!
AUTHOR: Samuel Low
DATE CREATED:   10 July 2021
'''

# --- Setup ---
import sqlite3
import pathlib
from datetime import date

blog = "blog/blog.db"

FIRST_RUN = True
if (pathlib.Path.cwd() / blog).exists():
    FIRST_RUN = False

con = sqlite3.connect(blog)
cursor = con.cursor()
# --- Functions ---

def setUpDB():
    global cursor

    cursor.execute('''
        CREATE TABLE
            posts (
                left TEXT,
                right TEXT
            )
    ;''')

    print("Created blog table!")

def menu():
    print('''
    Chose:
        1. Add a post
        2. Edit a post
        3. Delete a post
        4. Show all posts
        5. End 
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
    elif selection == 4:
        showPosts()
    else:
        finished = True

def addPost():
    global cursor

    post = ["",""]
    for i in range (2):

        if i == 0:
            print("Left Side")
        elif i == 1:
            print("Right Side")

        selection = 0
        while selection != 3:
            print('''
            Content Type:           
            1) Image
            2) Text
            3) Done''')

            selection = int(input(">"))
            content = formatContent(selection)
            if content != None:
                post[i] =  post[i] + content

    print(post)
    print("Formatted Blog Post!")

    cursor.execute('''
        INSERT INTO
            posts
        VALUES (
            ?, ?
        )
    ;''',post)

    con.commit()

    print("Post added to Table!")

def formatContent(selection):
    if selection == 1:
        content = input("Image name: ")
        content = "<img src=\"blog/images/" + content + "\">"
    elif selection == 2:
        content = input("Text: ")
        content = "<text>" + content + "</text>"
    else:
        content = None
    return content

def editPost():
    pass

def deletePost():
    pass

def showPosts():
    global cursor
    alll = cursor.execute('''
        SELECT
            *
        FROM
            posts
    ;''').fetchall()

    for x in alll:
        print(x)


# --- Main Program Code ---

if FIRST_RUN == True:
    setUpDB()

finished = False

print("Welcome to Your Horrible Text Based Blogging Program!")

while not finished:
    selection = menu()
    runFunction(selection)

print("Bye!")