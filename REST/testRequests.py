import urllib2
import requests
import pprint


r = requests.get('http://github.com')
#pprint.pprint(r.json())
#pprint.pprint(r.status_code)
#pprint.pprint(r.headers)

url = 'http://maps.googleapis.com/maps/api/directions/json'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url)
data = resp.json()
#pprint.pprint(data)



r = requests.get('https://api.github.com/events')
pprint.pprint(r.json())
