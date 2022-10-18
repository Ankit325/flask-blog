from flask import Flask, render_template, redirect

app = Flask(__name__,template_folder='templates',static_folder='static')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello2')
def hello_world2():
    return "<h1>Hello World 2</h1>"


@app.route("/redirect")
def redirect_to_index():
    return redirect("/")