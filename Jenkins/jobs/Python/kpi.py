from pprint import pprint
#import jenkins
from jenkinsapi.jenkins import Jenkins

username = 'ghebu'
password = 'passw0rd'
url = 'http://localhost:8080'
server = Jenkins(url, username, password)



def get_jobs():
    jobs = server.keys()
    pprint(jobs)
    #pprint(dir(server))

    return jobs

def get_scm_info_from_latest_successful_build():
    jobs = get_jobs()

    for job in jobs:
        job = server[job]
        lgb = job.get_last_good_build()
        print(lgb.get_revision())


if __name__ == '__main__':
    print(get_scm_info_from_latest_successful_build())