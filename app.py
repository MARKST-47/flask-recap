from flask import Flask, render_template, url_for
from employees import employees_data

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template('evaluate.html', title='Evaluate', number=num)

@app.route('/employees')
def employees():
    return render_template('employees.html', title='Employees', employees=employees_data)

# Dynamic URLs
@app.route('/welcome/<name>')
def welcome(name):
    return f'<h1>Hi {name.title()}, you are welcome to this page!</h1>'

@app.route('/addition/<int:num>') # Telling we expect an int parameter
def addition(num):
    return f"<h2>Input is {num}, Output is {num + 10}</h2>"

@app.route('/addition_two/<int:num1>/<int:num2>') # Telling we expect an int parameter
def addition_two(num1, num2):
    return f"<h2>Inputs are {num1} and {num2}, Output is {num1 + num2}</h2>"

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)
