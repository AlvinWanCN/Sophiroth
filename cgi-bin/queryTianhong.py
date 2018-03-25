#!/usr/bin/python3
# _*_ coding:utf-8 _*_
import urllib.request,re,time,json,os
from  bs4 import BeautifulSoup as BS
dirname=os.getcwd()
try:
    from modules.get_access_ip import getip
    gip = getip()
    access_ip = gip.ipinfo()
except:
    pass
thdict={}
totalFund=75941.89
totalMoney=96000
host='http://www.howbuy.com'
path='/fund/ajax/gmfund/valuation/valuationnav.htm'
querys='jjdm=000961'
url=host + path + '?' + querys
content = urllib.request.urlopen(url).read().decode('utf-8')
'''直接从原文匹配,相似内容比较少的情下比较方便使用这种方法，这里我们注释掉了，不用这种匹配方式
thdict['latestValue'] = re.findall(r'con.*\">(.*)<',content)[0] 
thdict['latestBenefit']= re.findall(r'con.*\">(.*)<',content)[1]
thdict['latestPercent']=re.findall(r'con.*\">(.*)<',content)[2]
'''
'''通过bs来匹配，找到指定类型的标签。找这里我们也注释掉了，不用这种匹配方式
content_list=BS(content,'lxml').find_all('span')
thdict['latestValue'] =re.findall(r'>(.*)<',str(content_list[0]))[0]  #通过BS查找指定属性后匹配
thdict['latestBenefit']= re.findall(r'>(.*)<',str(content_list[1]))[0]
thdict['latestPercent']=re.findall(r'>(.*)<',str(content_list[2]))[0]
'''
from lxml import etree #这里我们使用lxml 的etree，通过直接找xpath来找到内容
html=etree.HTML(content)
thdict['latestValue'] =html.xpath('/html/body/li/span[1]')[0].text #获取xpath的方法，可以谷歌浏览器里访问网站后，按F12，在Elements里找到我们的指定内容，然后右键——Copy——Copy XPath，然后把Xpath地址贴到这里来
thdict['latestBenefit']= html.xpath('/html/body/li/span[2]')[0].text #这里我们找的是列表里的text，除了text外，如果需要还可以获取tag和attrib
thdict['latestPercent']=html.xpath('/html/body/li/span[3]')[0].text
thdict['Nowtime']=time.strftime('%Y-%m-%d %H:%M:%S')
thdict['date']=re.sub(r'\s','%20',time.strftime('%Y-%m-%d %H:%M:%S'))
thdict['earnings'] = '%.2f' % float(float(thdict['latestValue'])*totalFund-totalMoney)
thdict['todayEarnings']='%.2f' % float(totalFund*float(thdict['latestBenefit']))
thdict['insertUrl']='http://47.75.0.56/cgi-bin/insertFund.py'
thdict['queryUrl']='http://47.75.0.56/cgi-bin/queryFund.py'
thdict.update(json.loads(urllib.request.urlopen('{queryUrl}'.format_map(thdict)).read().decode('utf-8')))
#print (thdict)
urllib.request.urlopen('{insertUrl}?value={latestValue}&percent={latestPercent}&date={date}'.format_map(thdict))
try:
    thdict['access_ip']=access_ip
    thdict['ipinfo']='上次访问IP地址：{access_ip} </br>'.format_map(thdict)
except:
    thdict['ipinfo']='Welcome </br>'
filename=os.path.join(os.path.dirname(__file__),'../html/tianhong.html')
htmlfile=open(filename,'r',encoding='UTF-8')
htmlcontent=htmlfile.read()
#print (htmlcontent)
htmlfile.close()
print("Content-type:text/html")
print()
print(htmlcontent.format_map(thdict))
