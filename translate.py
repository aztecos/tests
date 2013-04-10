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



def translator(from_l, to_l, string):
    language_pair = from_l + '|' + to_l
    parameters = {'q': string, 'langpair': language_pair}
    r = requests.get("http://api.mymemory.translated.net/get", params=parameters)
    print r.text

def main():
    translator(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__=='__main__':
    main()
