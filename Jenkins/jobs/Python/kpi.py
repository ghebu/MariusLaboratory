from pprint import pprint
#https://jenkinsapi.readthedocs.io/en/latest/index.html
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build

username = 'ghebu'
password = 'passw0rd'
url = 'http://localhost:8080'
server = Jenkins(url, username, password)
pprint(server.get_jobs_info())


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
            list_of_builds = [b for b in build.get_build_ids()]
            print(f"the job {job} has the builds {list_of_builds}")
            get_build_info(job, list_of_builds)
            lgb = build.get_last_good_build()
            git_url = lgb._get_git_repo_url()
            revision = lgb.get_revision()
            print(f"The build {build} with the # {lgb} has the revision {revision} and the git url {git_url}")
        except Exception as e:
            continue 

def get_build_info(job, builds=[]): 
    
    for build_no in builds: 
        build = Build(url, build_no, job)
        pprint(build)
    print(Build(url, 28, 'tests/warning').is_running())
       


if __name__ == '__main__':
    print(get_scm_info_from_latest_successful_build())