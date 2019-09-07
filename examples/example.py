import requests

code = """
a=1+2*3/4

def foo():
    pass
"""

params = {
  'code': code,
  'options': {'indent_size': 2}
}

url = 'http://127.0.0.1:5000/api/format'
resp = requests.get(url, params)
print(resp.text)
