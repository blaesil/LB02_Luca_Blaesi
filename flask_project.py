from functools import reduce

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Willkommen bei meinem Projekt'

#A1F Pure function----------------------------------------------------

@app.route('/add_numbers/<int:num1>/<int:num2>', methods=['GET'])
def add_numbers(num1, num2):
    result = num1 + num2
    return f'Die summe ist: {result}'

@app.route('/immutable', methods=['GET'])
def immutable():
    params = 1
    return f'Parameters: {params}'

#A1E Object Oriented----------------------------------------------------

class Math:
    def __init__(self, firstNumber, operator, secondNumber):
        self.firstNumber = firstNumber
        self.operator = operator
        self.secondNumber = secondNumber
        if operator == "+":
            self.result = firstNumber + secondNumber
        elif operator == "-":
            self.result = firstNumber - secondNumber
        elif operator == "*":
            self.result = firstNumber * secondNumber
        elif operator == "/":
            self.result = firstNumber / secondNumber

calculations = {
    1: Math(1, "+", 5),
    2: Math(5, "-", 2),
}

@app.route('/objectoriented/<int:num1>', methods=['GET'])
def objectoriented(num1):
    cal = calculations.get(num1)
    return jsonify({"result": cal.result})

#A1E Prozedural----------------------------------------------------

aufgaben = {
    "1 Aufgabe" : "1 + 5",
    "2 Aufgabe" : "5 - 2",
}

@app.route('/prozedural', methods=['GET'])
def prozedural():
    return jsonify(aufgaben)

#A1E Funktional----------------------------------------------------

def get_task(task_id):
    tasks = {
        1: Math(1, "+", 5),
        2: Math(5, "-", 2),
    }
    task = tasks.get(task_id)
    return task

@app.route('/funktional/<int:task_id>', methods=['GET'])
def funktional(task_id):
    task = get_task(task_id)

    if task:
        result = task.result
        return f"Das Ergebnis lautet: {result}"
    else:
        return "Aufgabe nicht gefunden."

#B1G----------------------------------------------------

@app.route('/algorithmic/<int:num1>/<int:num2>', methods=['GET'])
def berechne_summe1(num1, num2):
    result = num1 + num2
    return jsonify({"result": result})

#B1E und B1F----------------------------------------------------

def addiere_zahlen(zahl1, zahl2):
    return zahl1 + zahl2

@app.route('/teilfunktion/<int:num1>/<int:num2>', methods=['GET'])
def berechne_summe2(num1, num2):
    ergebnis = addiere_zahlen(num1, num2)
    return jsonify({'ergebnis': ergebnis})

#B2G und B2E----------------------------------------------------

def number(number):
    return f"Nummer, {number}"

nummer = number

@app.route('/object',  methods=['GET'])
def objekte():
    result = nummer(12)
    return result

#B2F----------------------------------------------------

def higher_function(func, num1, num2):
    result = func(num1, num2)
    return f"Das Ergebnis lautet: {result}"

def plus(num1, num2):
    return num1 + num2

@app.route('/hoeherwertige_funktion/<int:num1>/<int:num2>', methods=['GET'])
def run_higher_function(num1, num2):
    result = higher_function(plus, num1, num2)
    return result

#B3G----------------------------------------------------

lambda_plus = lambda a, b: a + b

@app.route('/lambda_expression', methods=['GET'])
def lambda_expression():
    result = lambda_plus(3, 5)
    return f"Ergebnis: {result}"

#B3F---------------------------------------------------

addition = lambda *args: sum(args)

@app.route('/lambda_expression2', methods=['GET'])
def lambda_expression2():
    numbers = [2, 4, 6, 8]
    result = addition(*numbers)
    return f"Ergebnis: {result}"

#B3E----------------------------------------------------

number_list = [11, 99, 3, 62, 43, 6]

sorted_numbers = sorted(number_list, key=lambda x: x)

@app.route('/lambda_expression3', methods=['GET'])
def run_lambda():
    return f"Sortierte Wörter nach Länge: {sorted_numbers}"

#B4G und B4E----------------------------------------------------

def verdoppeln(x):
    return x * 2

def ist_gerade(x):
    return x % 2 == 0

zahl_map_filter_reduce = [1, 2, 3, 4, 5]

verdoppelt = list(map(verdoppeln, zahl_map_filter_reduce))
gerade_zahlen = list(filter(ist_gerade, zahl_map_filter_reduce))
summe = reduce(lambda x, y: x + y, zahl_map_filter_reduce)

@app.route('/map', methods=['GET'])
def map():
    return f"Verdoppelt: {verdoppelt}"

@app.route('/filter', methods=['GET'])
def filter():
    return f"Gerade Zahlen: {gerade_zahlen}"

@app.route('/reduce', methods=['GET'])
def reduce():
    return f"Summe: {summe}"

#B4F----------------------------------------------------

'''verdoppelt_und_gefiltert = list(filter(ist_gerade, map(verdoppeln, zahl_map_filter_reduce)))
result_combined_map_filter_reduce = reduce(lambda x, y: x + y, verdoppelt_und_gefiltert)
@app.route('/combined', methods=['GET'])
def combined_map_filter_reduce():
    return f"Ergebnis: {result_combined_map_filter_reduce}"'''

#C1G und C1F und C1E----------------------------------------------------


#Gibt das Ergebnis der Berechnung als String zurück
def generate_calculation(result):
    return f"Das Ergebnis lautet: {result}"

#Berechnet das Ergebnis der beiden Zahlen
@app.route('/new/<int:num1>/<string:operator>/<int:num2>', methods=['GET'])
def lesbar(num1, operator, num2):
    calculation_instance = Math(num1, operator, num2)
    calculation_result = calculation_instance.result
    calculation = generate_calculation(calculation_result)
    return calculation


#Main----------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)