

def test_index(client):
  r = client.get('/')
  assert r.status_code == 200
  assert r.data == b'hello pyformatter'


def test_format(client):
  # TODO: add a few more test cases
  code = 'a=1+1 # bar'
  formatted = 'a = 1 + 1  # bar\n'

  data = {
    'code': code
  }
  r = client.get('/api/format', query_string=data)
  assert r.status_code == 200
  assert r.json['code'] == formatted


def test_indent_size(client):
  code = 'def foo():\n    pass\n'
  formatted = 'def foo():\n  pass\n'

  data = {
    'code': code,
    'indent_size': 2
  }
  r = client.get('/api/format', query_string=data)
  assert r.status_code == 200
  assert r.json['code'] == formatted
