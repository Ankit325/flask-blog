from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__,template_folder='templates',static_folder='static')

#Setting up SQL connection
sqliteConnection = sqlite3.connect('blog.db',check_same_thread=False)
cursor = sqliteConnection.cursor()

@app.route('/')
def hello_world():
    #read the data
    cursor.execute("SELECT * FROM name_table")
    na=cursor.fetchall()
    name=[]
    #print(na)
    for i in na:
        #print(i[0])
        name.append(i[0])
    return render_template('index.html', name=name)

@app.route('/hello2')
def hello_world2():
    return "<h1>Hello World 2</h1>"


@app.route("/redirect")
def redirect_to_index():
    return redirect("/")

@app.route("/fill-form", methods=["GET", "POST"])
def fillForm():
    #Method to take input
    if request.method=="POST": 
        name=request.form.get("name")
        #Create the data
        cursor.execute("INSERT INTO name_table (name) VALUES (?)", (name,))
        sqliteConnection.commit()
        #print(name)
        return redirect("/")
    return render_template("form.html")