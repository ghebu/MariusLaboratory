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
        try: 
            build = server[job]
            lgb = build.get_last_good_build()
            git_url = lgb._get_git_repo_url()
            revision = lgb.get_revision()
            print(f"The build {build} with the # {lgb} has the revision {revision} and the git url {git_url}")
        except Exception as e:
            continue 
       


if __name__ == '__main__':
    print(get_scm_info_from_latest_successful_build())