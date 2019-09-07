const https = require('https');
const querystring = require('querystring');

const code = `
a=1+2*3/4

def foo():
    pass
`;

params = querystring.stringify({
  code,
  indent_size: 2,
});

url = `https://pyformatter.com/api/format?${params}`;
https.get(url, res => {
  res.setEncoding('utf8');
  res.on('data', chunk => {
    console.log(JSON.parse(chunk)['code']);
  });
});
