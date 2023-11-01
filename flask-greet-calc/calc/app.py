# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

from operations import add, sub, mult, div

@app.route('/add')
def handle_add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(add(a,b))

@app.route('/sub')
def handle_sub():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(sub(a,b))

@app.route('/mult')
def handle_mult():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(mult(a,b))

@app.route('/div')
def handle_div():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return str(div(a,b))

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div,
}

@app.route("/math/<func>")
def do_math(func):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[func](a, b)

    return str(result)