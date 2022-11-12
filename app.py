from flask import Flask, render_template, redirect, request

app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index.html', name="World")

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
        #print(name)
        return render_template("index.html",name=name)
    return render_template("form.html")