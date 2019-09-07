import requests

code = """
a=1+2*3/4

def foo():
    pass
"""

params = {
  'code': code,
  'indent_size': 2
}

url = 'https://pyformatter.com/api/format'
resp = requests.get(url, params)
print(resp.json()['code'])
