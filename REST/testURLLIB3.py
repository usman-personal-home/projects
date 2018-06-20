import urllib2
import requests
import pprint


response = urllib2.urlopen('http://pythonforbeginners.com/')
print response.info()


r = requests.get('https://github.com/timeline.json')
pprint.pprint(r.json())
pprint.pprint(r.status_code)
