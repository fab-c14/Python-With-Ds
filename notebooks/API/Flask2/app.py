from flask import Flask,render_template, request, jsonify

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home_page():
    return render_template('index.html')

# @app.route("/")
# def hello_world():
#     return "<h1></h1>"
@app.route('/math',methods=['POST'])
def math_operation():
    if (request.method == 'POST'): # if its send through body
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if(ops == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if(ops == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if(ops == 'multiply'):
            r = num1 * num2
            result = 'the division of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if(ops == 'divide'):
            r = num1 / num2
            result = 'the division of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if(ops is None):
            result = 'Please Provide Data....'

        return render_template('results.html',result=result)

# lets say you are having json data 
@app.route('/postman_data',methods=['POST'])
def math_operation1():
    if (request.method == 'POST'): # if its send through body
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if(ops == 'add'):
            r = num1 + num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        if(ops == 'subtract'):
            r = num1 - num2
            result = 'the difference of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if(ops == 'multiply'):
            r = num1 * num2
            result = 'the division of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if(ops == 'divide'):
            r = num1 / num2
            result = 'the division of ' + str(num1) + ' and ' + str(num2) + " is " + str(r)
        
        if(ops is None):
            result = 'Please Provide Data....'

        return jsonify(result) #return it as a json object

if __name__ == "__main__":
    app.run(host="0.0.0.0")