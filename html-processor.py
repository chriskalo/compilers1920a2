import re

def myfunction(m):
  if (m.group(0)=='&amp;'):
    return '&'
  
  elif (m.group(0)=='&gt;'):
    return '>'

  elif (m.group(0)=='&lt;'):
    return '<'

  else:
    return ' '	

rexp1 = re.compile('<title>(.+?)</title>')	

rexp2 = re.compile('<!--.*?-->',re.DOTALL)

rexp3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL)

rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL)

rexp5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL)
rexp5_2 = re.compile(r'<.+?/>',re.DOTALL)

rexp6 = re.compile(r'&(amp|gt|lt|nbsp);')

rexp7 = re.compile(r'\s+')

with open('testpage.txt','r') as fp:

  text = fp.read()

  m = rexp1.search(text)
  
  print(m.group(1))	

  text = rexp2.sub(' ',text)

  text = rexp3.sub(' ',text)

  for m in rexp4.finditer(text):
    print('{}    {}'.format(m.group(1),m.group(2)))

  text = rexp5_1.sub(' ',text)
  text = rexp5_2.sub(' ',text)

  text = rexp6.sub(myfunction,text)

  text = rexp7.sub(' ',text)

  print(text)













