from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_number')
def random_number():
    return str(random.randint(10, 20))

if __name__ == '__main__':
    app.run(debug=True)
