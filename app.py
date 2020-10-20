from flask import Flask, render_template, redirect, request
import requests

app = Flask(__name__)

l = ('World', 'USA', 'Brazil', 'India', 'Russia', 'Peru', 'Chile', 'Mexico', 'South Africa', 'Spain', 'UK', 'Iran', 'Pakistan', 'Italy', 'Saudi Arabia', 'Turkey', 'Germany', 'Bangladesh', 'France', 'Colombia', 'Argentina', 'Canada', 'Qatar', 'Iraq', 'Egypt', 'Indonesia', 'Sweden', 'Ecuador', 'Belarus', 'Kazakhstan', 'Belgium', 'Oman', 'Philippines', 'Kuwait', 'Ukraine', 'UAE', 'Bolivia', 'Netherlands', 'Panama', 'Portugal', 'Dominican Republic', 'Singapore', 'Israel', 'Poland', 'Afghanistan', 'Romania', 'Bahrain', 'Nigeria', 'Armenia', 'Switzerland', 'Guatemala', 'Honduras', 'Azerbaijan', 'Ireland', 'Ghana', 'Japan', 'Algeria', 'Moldova', 'Serbia', 'Austria', 'Nepal', 'Morocco', 'Cameroon', 'Uzbekistan', 'S. Korea', 'Czechia', 'Ivory Coast', 'Denmark', 'Kyrgyzstan', 'Kenya', 'El Salvador', 'Australia', 'Sudan', 'Venezuela',
'Norway', 'Costa Rica', 'Malaysia', 'North Macedonia', 'Senegal', 'DRC', 'Ethiopia', 'Bulgaria', 'Bosnia and Herzegovina', 'Palestine', 'Finland', 'Haiti', 'Tajikistan', 'French Guiana', 'Guinea', 'Gabon', 'Madagascar', 'Mauritania', 'Luxembourg', 'Djibouti', 'CAR', 'Hungary', 'Croatia', 'Greece', 'Albania', 'Thailand', 'Paraguay', 'Nicaragua', 'Somalia', 'Equatorial Guinea', 'Maldives', 'Mayotte', 'Sri Lanka', 'Malawi', 'Lebanon', 'Cuba', 'Mali', 'Congo', 'South Sudan', 'Estonia', 'Slovakia', 'Iceland', 'Lithuania', 'Guinea-Bissau', 'Slovenia', 'Zambia', 'Cabo Verde', 'Sierra Leone', 'Hong Kong', 'Libya', 'New Zealand', 'Yemen', 'Eswatini', 'Rwanda', 'Mozambique', 'Benin', 'Tunisia', 'Montenegro', 'Jordan', 'Latvia', 'Niger', 'Zimbabwe', 'Liberia', 'Uganda', 'Burkina Faso', 'Namibia', 'Cyprus', 'Uruguay', 'Georgia', 'Chad', 'Andorra', 'Suriname', 'Jamaica', 'Togo', 'Sao Tome and Principe', 'Diamond Princess', 'San Marino', 'Malta', 'Réunion', 'Channel Islands', 'Angola', 'Tanzania', 'Syria', 'Taiwan', 'Botswana', 'Vietnam', 'Mauritius', 'Myanmar', 'Isle of Man', 'Comoros', 'Guyana', 'Burundi', 'Mongolia', 'Lesotho', 'Martinique', 'Eritrea', 'Cayman Islands', 'Guadeloupe', 'Faeroe Islands', 'Gibraltar', 'Cambodia', 'Bermuda', 'Brunei', 'Trinidad and Tobago', 'Bahamas', 'Monaco', 'Aruba', 'Barbados', 'Seychelles', 'Liechtenstein', 'Bhutan', 'Sint Maarten', 'Antigua and Barbuda', 'Turks and Caicos', 'Gambia', 'French Polynesia', 'Macao', 'Saint Martin', 'Belize', 'St. Vincent Grenadines', 'Curaçao', 'Fiji', 'Timor-Leste', 'Grenada', 'New Caledonia', 'Saint Lucia', 'Laos', 'Dominica', 'Saint Kitts and Nevis', 'Falkland Islands', 'Greenland', 'Montserrat', 'Vatican City', 'Papua New Guinea', 'Western Sahara', 'MS Zaandam', 'Caribbean Netherlands', 'British Virgin Islands', 'St. Barth', 'Anguilla', 'Saint Pierre Miquelon', 'China')

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
