from flask import Flask, render_template, url_for, redirect, request
from soapclient import startcalculate
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/calc', methods=['POST', 'GET'] )
def calc():
    r = request.args.get('s', '2+2')
    print r
    return startcalculate('localhost', 8080, r)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error = error), 404

if __name__ == '__main__':
    app.run(debug=True)
