from flask import Flask,render_template
app = Flask(__name__)


@app.route('/arnab')
def arnab():
    return render_template('arnab.html')


@app.route('/tushar')
def tushar():
    return render_template('tushar.html')


app.run(debug=True)