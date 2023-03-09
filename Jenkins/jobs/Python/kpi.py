from pprint import pprint
import jenkins
from jenkins.Jenkins import Jenkins

username = 'ghebu'
password = 'passw0rd'
url = 'http://localhost:8080'

def getSCMInfroFromLatestGoodBuild():
    server = Jenkins(url, username, password)
    print(server)
    pprint(dir(server))
    # jobs = J[jobName]
    # lgb = job.get_last_good_build()
    # return lgb.get_revision()

if __name__ == '__main__':
    print(getSCMInfroFromLatestGoodBuild())