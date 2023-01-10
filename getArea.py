import urllib.request
import urllib.parse

data = {}

data['lat'] = '34.144442'
data['lon'] = '-118.654084'
data['censusYear'] = '2020'
data['format'] = 'json'

urlVal = urllib.parse.urlencode(data);

# https://geo.fcc.gov/api/census/area?lat=34.144442&lon=-118.654084&censusYear=2020&format=json

url = 'https://geo.fcc.gov/api/census/area';
fullUrl = url + '?' + urlVal;

#print(fullUrl);
header = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
request = urllib.request.Request(fullUrl, headers=header)
reponse = urllib.request.urlopen(request).read()
print(reponse);

