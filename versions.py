#coding=utf-8  
import paramiko

class VersionsInfo:
    
    def ssh_connect(self, _host, _username, _password ):
        try:
            _ssh_fd = paramiko.SSHClient()
            _ssh_fd.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
            _ssh_fd.connect( _host, username = _username, password = _password )
        except Exception, e:
            print( 'ssh %s@%s: %s' % (_username, _host, e) )
            exit()
        return _ssh_fd


    def ssh_exec_cmd(self, _ssh_fd, _cmd ):
        return _ssh_fd.exec_command( _cmd )

    
    def ssh_close(self, _ssh_fd ):
        _ssh_fd.close()


    def verinfo(self):
        verlist=[]
        sshd = self.ssh_connect( 'lunkrauto02.rd.mt', 'root','pass123,./' )
        #sshd = self.ssh_connect( 'lunkrauto02.rd.mt', 'root', 'pass123,./' )
        stdin, stdout, stderr = self.ssh_exec_cmd( sshd, 'cat /home/coremail/versions.txt' )
        err_list = stderr.readlines()
        if len( err_list ) > 0:
            print 'ERROR:' + err_list[0]
            exit()
        for item in stdout.readlines():
            list1=item.split(':')
            verlist.append(list1)
 #       print item
        self.ssh_close( sshd )
        webv=verlist[1][1]
        wmv=verlist[0][1]
        stat=u'一、测试版本信息'
        webName=u'Web端版本'
        wmName=u'后端版本'
        bro=u'浏览器'
        brover='Chrome 55.0.2883.87 m'
        env=u'测试环境'
        envlink='http://lunkrauto02.rd.mt/lunkr'
        
        report='<h2>'+stat+'</h2>'+ '''<table class="gridtable">
    <tr>
	    <th>'''+ webName+'''</th><td align="center">'''+webv+'''</td>
    </tr>
    <tr>
	    <th align="center">'''+wmName+'''</th><td align="center">'''+wmv+'''</td>
    </tr>
    <tr>
	    <th align="center">'''+bro+'''</th><td align="center">'''+brover+'''</td>
    </tr>
    <tr>
	    <th align="center">'''+env+'''</th><td align="center">'''+envlink+'''</td>
    </tr>
    </table>'''
        return report
        
if __name__=='__main__':
    ver=VersionsInfo()
    a=ver.verinfo()
    print a
