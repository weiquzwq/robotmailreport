#coding=utf-8
import re
import urllib
import urllib2
import sys
import time
import json
from SendReport import Report
from TotalReport import TotalTest
from versions import VersionsInfo
reload(sys)
sys.setdefaultencoding('utf-8')
class HtmlReport:
    
    def gettotal(self,url):
        req=urllib2.Request(url)
        response=urllib2.urlopen(req)
        return response
    
    def getHtml(self,url):
        page = urllib.urlopen(url)
        html = page.read()
        html=html.decode('utf-8')
        return html

    def getfailtest(self,html):
        reg =r'<h2>Failed Test Cases</h2>(.+?)<h2>Test Suites</h2>'
        imgre = re.compile(reg)
        htmllist = re.findall(imgre,html)
        return htmllist

    def gettr(self,html):
        reg =r'<tr>(.+?)</tr>'
        imgre = re.compile(reg)
        htmllist = re.findall(imgre,html)
        return htmllist

    def gettd(self,html):
        reg =r'<td (.+?)</td>'
        imgre = re.compile(reg)
        htmllist = re.findall(imgre,html)
        return htmllist

if __name__=='__main__':
    #req=urllib2.Request("http://lunkrauto01.rd.mt:1234/job/Lunkr4WebAuto/282/buildNumber")
    req=urllib2.Request("http://jenkins.rd.mt:1234/job/Lunkr4WebAuto/lastBuild/buildNumber")
    response=urllib2.urlopen(req)
    abc=json.load(response)
    buildtime=str(abc)
#    buildtime=str(73)
    print buildtime

#1、测试详情部分
    f=open('teststyle.css')
    htmlstyle=f.read()
    f.close()
    url="http://jenkins.rd.mt:1234/job/Lunkr4WebAuto/"+buildtime+"/robot/"
    report_url=url+'report/report.html'
    info=u'三、测试详情可点击以下链接'
    baseinfo=u'Lunkr4Web测试概况总览'
    autoRe=u'Lunkr4Web自动化测试报告'
    autolog=u'Lunkr4Web自动化测试输出日志'
    infolink='<h2>'+info+'</h2>'+'''<ul class="square"><li><h3><a href="'''+url+'''">'''+baseinfo+'''</a></h3></li>
<li><h3><a href="'''+url+'''report/report.html">'''+autoRe+'''</a></h3></li>
<li><h3><a href="'''+url+'''report/log.html">'''+autolog+'''</a></h3></li></ul>'''

#2、测试版本远程获取
    ver=VersionsInfo()
    result=ver.verinfo()
    
#3、测试基本统计部分
    totalstat=TotalTest()
    totalhtml=totalstat.maketotalreport(url)

#4、失败用例部分
    report=HtmlReport()
    
    html = report.getHtml(url)
    tdlist=[]
    tdflist=[]
    ftlist=[]
    i=0
    failtest =report.getfailtest(html)
    str1=('').join(failtest)
    trlist=report.gettr(str1)
    for flist in trlist:
        fstr=('').join(flist)
        tdlist.append(report.gettd(fstr))
    
    hao=u'序号'
    ming=u'失败测试用例'
    che=u'四、失败的测试用例（点击用例名称可查看详情）'
    tou='<p><tr><th>'+hao+'</th><th align="center">'+ming+'</th></tr></p>'
    for tlist in tdlist:
        tstr=('').join(tlist[0])
        num=str(i)
        ftstr='<p><tr><td align="center">'+num+'</td><td '+tstr+'</td></tr></p>'
        tdflist.append(ftstr)
        i=i+1
    
    for tdf in tdflist:
        tdfstr=('').join(tdf)
        strlist=tdfstr.split('<a href="')
        failstr=strlist[0]+'<a href="'+url+strlist[-1]
        ftlist.append(failstr)
#        print failstr
#        print '\n'

    fttlist=ftlist[1:]
    if len(fttlist)>20:
        morefail=u'更多失败的测试用例可点击本链接查看'
        tmplist=fttlist[:20]
        moreinfo='''<tr><td><font size="3" color="red">more</font></td><td align="center"><a href="'''+report_url+'''"><font size="3" color="red">'''+ morefail+'''</font></a></td></tr>'''
        tmplist.append(moreinfo)
        fttlist=tmplist
    failhtml=('').join(fttlist)
    if failhtml.strip()=='':
        failhtml=u'测试通过，没有失败的测试用例'
        fhtml=htmlstyle+result+totalhtml+infolink+'<h2>'+che+'</h2>'+'<tr><td><font size="3" color="green">'+failhtml+'</font></td></tr>'
    else:   
        fhtml=htmlstyle+result+totalhtml+infolink+'<h2>'+che+'</h2>'+'<table class="gridtable">'+tou+failhtml+'</table>'
#    totalurl=url+'api/json?pretty=true'
#    resq=TotalTest.gettotal(totalurl)
#    dict1=json.load(resq)
#    print dict1, type(dict1)
    Report.sendReport(fhtml)
