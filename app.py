from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/india')
def india():
    return render_template('india.html')

@app.route('/india', methods=['POST'])
def indiacases():
    stateName = request.form['state']
    url = f'https://api.covid19india.org/data.json'
    req = requests.get(url)
    res1 = req.json()
    for i in range(len(res1['statewise'])):
        res = res1['statewise'][i].items()
        if ('state', stateName) in res:
            res2 = dict(res)
    state = res2['state']
    active = res2['active']
    confirmed = res2['confirmed']
    deaths = res2['deaths']
    recovered = res2['recovered']
    return render_template('indiacases.html', state=state, active=active, recovered=recovered, confirmed=confirmed, deaths=deaths)

@app.route('/cases', methods=['POST'])
def cases():
    ctry = request.form['country']
    url = f'https://coronavirus-19-api.herokuapp.com/countries/{ctry}'
    req = requests.get(url)
    res = req.json()
    country = res['country']
    casess = res['cases']
    deaths = res['deaths']
    todayDeaths = res['todayDeaths']
    recovered = res['recovered']
    active = res['active']
    critical = res['critical']
    totalTests = res['totalTests']
    return render_template('cases.html', country=country, casess=casess, deaths=deaths, todayDeaths=todayDeaths, recovered=recovered, active=active, critical=critical, totalTests=totalTests)

@app.errorhandler(500)
def error_500(error):
    return render_template('500.html') , 500

if __name__ == '__main__':
    app.run()
