
import requests
r = requests.get('https://corona.lmao.ninja/countries')
for i in r.json():
    print('Country: ',i['country'], 'Cases: ',i['cases'])