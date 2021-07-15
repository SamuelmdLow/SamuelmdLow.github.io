from flask import Flask, render_template, request, redirect
import sqlite3

blog = "blog/blog.db"

con = sqlite3.connect(blog)
cursor = con.cursor()

posts = cursor.execute('''
    SELECt
        *
    FROM
        posts
''').fetchall()

print(posts)

app = Flask(__name__)