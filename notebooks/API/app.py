from flask import Flask
from flask import request
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World! </h1>"
    # purpose run application - create client and server architecture
    # server should be open
    # and client will access server funtions
    # # one route contains one function

@app.route("/hello_world1")
def hello_world1():
    return "<h1>Hello World 1</h1>"


@app.route("/hello_world2")
def hello_world2():
    return "<h1>Hello World 2</h1>"

@app.route("/test")
def test():
    a = 5 + 6
    # return "function to run app" + str(a)
    return "function to run app {}".format(a)

# functions which take query parameter
@app.route("/test2")
def test2():
    data = request.args.get("x")
    return "this is a data input from my url {}".format(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0")