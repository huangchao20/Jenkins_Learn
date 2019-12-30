import datetime, time
from jenkinsapi.jenkins import *
from jenkinsapi.job import *
from jenkinsapi.build import Build
def Url_Get_Job_List(url, username, password):
    print(username)
    print(password)
    jenkins = Jenkins(url, username, password)
    # keys = ['http:/192.168.0.104:8090/Deploy_02', 'http:/192.168.0.104:8090/package_01', 'http:/192.168.0.104:8090/SVN_server', 'http:/192.168.0.104:8090/Svn_Test_01']
    # job_name = 'http:/192.168.0.104:8090/Deploy_02'
    # my_job = jenkins.get_job(job_name)
    # print(my_job)
    count = 0
    print(jenkins.keys())
    for job_name in jenkins.keys():
        # my_job = jenkins.get_job(job_name)
        count = count + 1
        #print “Job” + str(count) + " : "+job_name
        print(job_name)
if __name__ == "__main__":
    url = 'http://172.20.10.11:8090'
    username = '17524'
    password = 'cs123456'
    # url = input('jenkins地址:')
    # username = input('jenkins账号:')
    # password = input('密码:')
    Url_Get_Job_List(url, username, password)
