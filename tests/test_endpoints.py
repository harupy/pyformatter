

def test_index(client):
  r = client.get('/')
  assert r.status_code == 200


def test_format(client):
  cases = [
    {
      'before': 'a=1+2*3/4\n',
      'after': 'a = 1 + 2 * 3 / 4\n'
    },
    {
      'before': 'a = 1\n\n\n',
      'after': 'a = 1\n'
    },
    {
      'before': 'a =   1\n',
      'after': 'a = 1\n'
    },
    {
      'before': 'a = 1 # foo\n',
      'after': 'a = 1  # foo\n',
    },
    {
      'before': 'def foo():\n  pass\n',
      'after': 'def foo():\n    pass\n',
    },
    {
      'before': 'def foo():\n    pass\n',
      'after': 'def foo():\n  pass\n',
      'options': {'indent_size': 2}
    }
  ]

  for case in cases:
    data = {
      'code': case.get('before'),
      **case.get('options', {})
    }
    r = client.get('/api/format', query_string=data)
    assert r.status_code == 200
    assert r.json['code'] == case['after']
