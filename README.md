# Pyformatter

REST API to format python code.

https://pyformatter.com

## Getting Started

```console
# if pipenv is not installed yet
pip install pipenv

# force pipenv to create .venv in the current directory
export PIPENV_VENV_IN_PROJECT=1

# install dependencies
pipenv install

# run the app
python run.py
```

## Run with Docker

```
docker-compose up
```

## Example in Python

see [examples](./examples).

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
flake8 -v
python -m pytest
```

## Todos

- Add an option which allows users to choose a code formatter. The current version only supports `autopep8`.

## References

- [Miserlou/Zappa: Serverless Python](https://github.com/Miserlou/Zappa)
- [hhatto/autopep8: A tool that automatically formats Python code to conform to the PEP 8 style guide.](https://github.com/hhatto/autopep8)
