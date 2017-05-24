#coding=utf-8
import urllib
import urllib2
import sys
import time
import json
from SendReport import Report

class TotalTest:

    @staticmethod
    def gettotal(url):
        req=urllib2.Request(url)
        response=urllib2.urlopen(req)
        return response


    def maketotal(self,url):
    	#print url
        req=TotalTest.gettotal(url)
        dict1=json.load(req)
        return dict1['overallTotal'],dict1['overallPassed'],dict1['overallFailed'],dict1['passPercentage']

    def maketotalreport(self,url):
        totalurl=url+'api/json?pretty=true'
        t,pt,ft,p=self.maketotal(totalurl)
        print t,pt,ft,p
        if p<95:
            testre='<font color="red">FAIL</font>'
        elif p>=95 and p<100:
            testre='<font color="orange">STABLE</font>'
        else:
            testre='<font color="green">PASS</font>'
       
        totalName=u'执行用例数'
        passTest=u'通过用例数'
        failName=u'失败用例数'
        passName=u'通过率'
        testName=u'测试结果'
        stat=u'二、测试用例统计'
        report='<h2>'+stat+'</h2>'+ '''<table class="gridtable">
    <tr>
	    <th>'''+ totalName+'''</th><th>'''+passTest+'''</th><th>'''+failName+'''</th><th>'''+passName+'''</th><th>'''+testName+'''</th>
    </tr>
    <tr>
	    <td align="center">'''+str(t)+'''</td><td align="center"><font color="green">'''+str(pt)+'''</font><td align="center"><font color="red">'''+str(ft)+'''</font></td><td align="center">'''+str(p)+'''%</td><td align="center">'''+testre+'''</td>
    </tr>
    </table>'''
        return report
