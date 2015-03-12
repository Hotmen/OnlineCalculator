from flask import Flask, render_template, url_for, redirect, request, flash
from soapclient import startcalculate
import polishrecord

conf = {
    'mode': 'SOAP',
    'server': 'localhost',
    'port': 8080
}

app = Flask(__name__)
app.config['SECRET_KEY'] ='secretverykey'

@app.route('/')
def index():
    return render_template('main.html', mode=conf['mode'])


@app.route('/options', methods=['GET', 'POST'])
def options():
    if request.method == 'POST':
        conf['mode'] = request.form['type']
        conf['server'] = request.form['server']
        conf['port'] = request.form['port']
        flash('Settings successful saved')
    return render_template('options.html', conf=conf)


@app.route('/calc', methods=['GET'])
def calc():
    r = request.args.get('s', '2+2')
    if conf['mode'] == 'SOAP':
        return startcalculate(conf['server'], int(conf['port']), r)
    return str(polishrecord.polish(polishrecord.exptopolish(str(r))))


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html', error=err), 404

if __name__ == '__main__':
    app.run(debug=True)
