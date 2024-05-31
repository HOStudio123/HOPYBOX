from requests import get
from bs4 import BeautifulSoup

class NullError(Exception):
    def __init__(self):
        super().__init__('No result can be find')
        
class Translate:
  class Google:
    def trans(self,word,tl):
      res = get(f'http://translate.google.com/translate_a/single?client=at&sl=auto&tl={tl}&dt=t&q={word}')
      return res.json()[0][0][0]   
  class YouDao:
    def trans(self,word,tl):
      res = get(f'https://dict.youdao.com/result?word={word}&lang=en')
      soup = BeautifulSoup(res.text,'html.parser')
      data = self.word(soup,tl)
      if data:
        return data
      else:
        return self.sentence(soup)
    def word(self,soup,tl):
      if tl == 'zh-CN':
        data = dict()
        word = soup.select('span.trans')
        pos = soup.select('span.pos')
        for i in range(len(word)):
          if i >= len(pos):
            data[word[i].text] = ''
          else:
            data[word[i].text] = pos[i].text
        return data
      else:
        data = list()
        word = soup.select('div.trans-ce a.point')
        for i in range(len(word)):
          data.append(word[i].text)
        return data
    def sentence(self,soup):
      content = soup.select('p.trans-content')
      if content:
        return content[0].text
      else:
        raise NullError
        
translate = Translate()