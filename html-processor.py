import re

def myfunction(m):  #ilopoihsh sunarthshs pou tha kaleite meso ths sub kai tha epistrefei to antistoixo string kathe fora analoga pou to teriasma pou exei ginei 
  if (m.group(0)=='&amp;'):
    return '&'
  
  elif (m.group(0)=='&gt;'):
    return '>'

  elif (m.group(0)=='&lt;'):
    return '<'

  else:
    return ' '	

rexp1 = re.compile('<title>(.+?)</title>')	#teriasma tou tag <title></title> mesa sto keimeno mazi me to periexomeno tou

rexp2 = re.compile('<!--.*?-->',re.DOTALL)  #teriasma olwn twn sxoliwn mesa sto keimeno mazi me to periexomeno tous

rexp3 = re.compile(r'<(s(?:cript|tyle)).*?>.*?</\1>',re.DOTALL) #teriasma olwn twn tag <script></script> kai <style></style> mesa sto keimeno mazi me to periexomeno tous

rexp4 = re.compile(r'<a.+?href="(.*?)".*?>(.*?)</a>',re.DOTALL) #teriasma olwn twn tag <a></a> mesa sto keimeno mazi me to periexomenos tous

rexp5_1 = re.compile(r'<.+?>|</.+?>',re.DOTALL) #teriasma olwn twn tag pou exoun morfh p.x <a> h </a> 
rexp5_2 = re.compile(r'<.+?/>',re.DOTALL) #teriasma olwn twn tag  pou exoun morfh p.x <meta charset="utf-8" />

rexp6 = re.compile(r'&(amp|gt|lt|nbsp);') # teriasma olwn twn akolouthiwn pou exoun morfh &amp; h &gt; h &lt; h &nbsp; mesa sto keimeno

rexp7 = re.compile(r'\s+') #teriasma akolouthiwn sinexomenwn xarakthrwn whitespace

with open('testpage.txt','r') as fp:

  text = fp.read() #eisagwgh tou html keimenou mesa sthn metavlhth text

  m = rexp1.search(text) #anazhthsh gia teriasma simfona me thn mhxanh teriasmatos rexp1(parapanw perigrafetai h kanonikh ekfrash vash ths opoias kanei anazhthsh tairiasmatos h rexp1)
  
  print(m.group(1))	#ektiposh merous tou teriasmatos(titlos) pou vrike h mhxanh teriasmatos rexp1

  text = rexp2.sub(' ',text) #apaloifh olwn twn sxoliwn tou keimenou mazi me to periexomeno tous

  text = rexp3.sub(' ',text) #apaloifh olwn twn tag <script></script> kai <style></style> mesa sto keimeno mazi me to periexomeno tous

  for m in rexp4.finditer(text): #anazhthsh kathe pithanou teriasmatos mesa sto keimeno simfona me thn mhxanh teriasmatos rexp4(parapanw perigrafetai h kanonikh ekfrash vash ths opoias kanei anazhthsh tairiasmatos h rexp4)
    print('{}    {}'.format(m.group(1),m.group(2))) #ektiposh merous tou teriasmatos(sindesmos kai periexomeno metaksi <a> kai </a>) pou vrike h mhxanh teriasmatos rexp4

  text = rexp5_1.sub(' ',text) #apaloifh olwn twn tag tou keimenou ths morfhs <a> h </a>
  text = rexp5_2.sub(' ',text) #apaloifh olwn twn tag tou keimenou ths morfhs <meta charset="utf-8" />

  text = rexp6.sub(myfunction,text) #antikatastash olwn twn akolouthown tou keimenou pou exoun morfh &amp; h &gt; h &lt; h &nbsp; vash tou pinaka pou exei dothei sthn ekfonhsh

  text = rexp7.sub(' ',text) #antikatastash akolouthiwn sinexomenwn xarakthrwn whitespace me ena xarakthra whitespace

  print(text) #ektipwsh tou keimenou me oles tis tropopoihseis pou tou exoun ginei parapanw













