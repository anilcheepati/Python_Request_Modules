import requests

r = requests.put('https://httpbin.org/put', data={'key': 'value'})
s = requests.delete('https://httpbin.org/delete')
t = requests.head('https://httpbin.org/get')
u = requests.options('https://httpbin.org/get')

print(u.text)