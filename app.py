import os
from flask import Flask, render_template

app = Flask(__name__)

# Homepage
@app.route('/')
def home():
    return render_template('index.html')


# Number Guessing Game
@app.route('/guess')
def guess():
    return render_template('guess.html')


# Rock Paper Scissors
@app.route('/rps')
def rps():
    return render_template('rps.html')


# Memory Cards Game
@app.route('/memory')
def memory():
    return render_template('memory.html')


# Reaction Speed Test
@app.route('/reaction')
def reaction():
    return render_template('reaction.html')


# Run application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))

    app.run(
        host='0.0.0.0',
        port=port,
        debug=False
    )