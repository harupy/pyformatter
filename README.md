# Pyformatter

https://pyformatter.com

## Example

```python
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

```

The output looks like:

```python

a = 1 + 2 * 3 / 4


def foo():
  pass

```

## Test

```
python -m pytest
```

## Ref.

- [Miserlou/Zappa: Serverless Python](https://github.com/Miserlou/Zappa)
- [Build a Python REST API with Serverless, Lambda, and DynamoDB](https://serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/)
