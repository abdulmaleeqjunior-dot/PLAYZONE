import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/guess')
def guess():
    return render_template('guess.html')

@app.route('/rps')
def rps():
    return render_template('rps.html')

@app.route('/memory')
def memory():
    return render_template('memory.html')

@app.route('/reaction')
def reaction():
    return render_template('reaction.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
