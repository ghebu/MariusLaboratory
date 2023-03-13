from pprint import pprint
#https://jenkinsapi.readthedocs.io/en/latest/index.html
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build
import requests
from datetime import datetime


username = 'ghebu'
password = 'passw0rd'
jenkins_url = 'http://localhost:8080'
server = Jenkins(jenkins_url, username, password)

# build_obj = Build('http://localhost:8080/', 17, 'python-kpi')
# pprint(f"BUILD INFO: {build_obj}")

jenkins_crumb = requests.get(f'{jenkins_url}/crumbIssuer/api/json', auth=(username, password)).json()

def get_jobs():
    # jobs = server.keys()
    jobs = [z for z in server.get_jobs_info()]
    pprint(jobs)
    return jobs

def get_scm_info_from_latest_successful_build():
    jobs = get_jobs()
    print(jobs)
    for job in jobs:
        print(f"JOB: {job}")
        try: 
            build = server[job[1]]
            list_of_builds = [b for b in build.get_build_ids()]
            
            job_url =job[0]
            print(get_build_info(job_url, list_of_builds))
            
            print(f"the job {job[1]} has the builds {list_of_builds}")
            
            #pprint(dir(build)) #functions: get_last_buildnumber, http://localhost:8080/job/python/job/python-kpi/19/console
            
            lgb = build.get_last_good_build()
            git_url = lgb._get_git_repo_url()
            revision = lgb.get_revision()
            print(f"The build {build} with the # {lgb} has the revision {revision} and the git url {git_url}")
        except Exception as e:
            continue 


       

def get_build_info(job_url, list_of_builds):
    
    job_results = {}


    for build in list_of_builds:
        
        response = requests.get(f'{job_url}/{build}/api/json', 
                                auth=(username, password),
                                headers={jenkins_crumb['crumbRequestField'] : jenkins_crumb['crumb']}).json()
        
        ##Get the job timestamp
        timestamp = int(str(response['timestamp'])[:10])
        timestamp_human_readable = datetime.fromtimestamp(timestamp).isoformat()


        payload = {
            'url' : job_url,
            'build' : build,
            'author' : 'TODO',
            'git_url' : 'TODO',
            'timestamp': timestamp_human_readable
        }


        if job_url not in job_results:
            job_results[job_url] = payload 
        else:
            job_results[job_url] += payload
        
        pprint(response)
        return job_results


if __name__ == '__main__':
    print(get_scm_info_from_latest_successful_build())
    



# TESTS
#get_joburl_and_name = [z for z in server.get_jobs_info()]