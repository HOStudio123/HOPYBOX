import requests as visit
def translate_print(word):
  ''' YouDao translate '''
  url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
  data = {
'i':word,
'from':'AUTO',
'to':'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'doctype': 'json',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false'
}
  res = visit.post(url,data=data)
  answer = res.json()
  result = answer["translateResult"][0][0]["tgt"]
  print('\033[92m{}'.format(result))

def translate(word):
  url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
  data = {
'i':word,
'from':'AUTO',
'to':'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'doctype': 'json',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false'
}
  res = visit.post(url,data=data)
  answer = res.json()
  result = answer["translateResult"][0][0]["tgt"]
  return result