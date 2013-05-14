import sys
import requests
import json
import argparse

#USAGE


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

def translator(f, t, s):
    language_pair = f + '|' + t
    parameters = {'q': s, 'langpair': language_pair}
    r = requests.get("http://api.mymemory.translated.net/get", params=parameters)
    json_data = r.text
    data = json.loads(json_data)
    print data['responseData']['translatedText']

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--from", dest = "frm", help="Language code of the language you wanted translated from")
    parser.add_argument("-t", "--to", dest = "to", help="Language code of the language you wanted translated to")
    parser.add_argument("-s", "--string", dest = "string", help="String to be translated")
    args = parser.parse_args()
    translator(args.frm, args.to, args.string)

if __name__=='__main__':
    main()
