import os
from flask import Flask, abort, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('calc.html')


@app.route('/calculadora', methods=["POST", "GET"])
def calculadora():
    value1 = request.form['number1']
    value2 = request.form['number2']
    operator = request.form['operator']

    value1 = int(value1)

    value2 = int(value2)

    if(operator == 'sum'):
        resutCalc = value1 + value2
    elif(operator == 'mult'):
        resutCalc = value1 * value2
    elif(operator == 'min'):
        resutCalc = value1 - value2
    elif(operator == 'div'):
        if(value2 == 0):
            abort(422)
        else:
            resutCalc = value1 / value2
    else:
        abort(404)

    return str(resutCalc)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='127.0.0.1', port=port)
