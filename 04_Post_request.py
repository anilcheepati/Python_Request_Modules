import requests

r=requests.post('https://httpbin.org/post?a=b', data={'anil': 'good'})
print(r.text)