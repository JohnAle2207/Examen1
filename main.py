from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = '1234'

@app.route('/ingresar', methods=['GET', 'POST'])
def ingresar():
    print('Hola')
    return render_template('ingresar.html')

if __name__ == '__main__':
    app.run(debug=True, port=8008)
