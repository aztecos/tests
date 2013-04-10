import sys
import requests

#NOTE:urllib is not working as expected. 
# import sys

# def translate(from_l, to_l, string):

# import urllib
# import urllib2

# url = 'http://api.mymemory.translated.net/get'

# values = {'q': 'Hello', 'langpair': 'en|it'}

# data = urllib.urlencode(values)
# req = urllib2.Request(url, data)
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page
#-------------------------------------------------------------------------------------#

payload = {'q': 'Hello', 'langpair': 'en|it'}
r = requests.get("http://api.mymemory.translated.net/get", params=payload)
print r.text
