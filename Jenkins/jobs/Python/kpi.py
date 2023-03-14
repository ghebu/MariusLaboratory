#https://www.programiz.com/python-programming/online-compiler/?ref=3170d3c3 -- online compiler

from pprint import pprint
#https://jenkinsapi.readthedocs.io/en/latest/index.html
from jenkinsapi.jenkins import Jenkins
from jenkinsapi.build import Build
import requests
from datetime import datetime

"""
TODO

Get build duration

"""
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
            short_job_name = job[1]
            build = server[short_job_name]
            list_of_builds = [b for b in build.get_build_ids()]   ##The method doesn't work for some of the builds
            
            try:
                git_url = build.get_last_build()._get_git_repo_url()  
            except Exception as e: 
                git_url = None

            job_url =job[0]

            print(f"The job {short_job_name} has the builds {list_of_builds}. ")
            print(f"requirements for get_build_info: {job_url}, {short_job_name}, {list_of_builds}, {git_url}")
            pprint(get_build_info(job_url, short_job_name, list_of_builds, git_url))
            

        
        except Exception as e:
            continue 


       

def get_build_info(job_url, job_name, list_of_builds, git_url):
    
    job_results = {}

    department = None
    if 'bitbucket' in git_url: 
        department = git_url.split('/')[3].replace('.git','')  if 'http' in git_url else git_url.split('/')[5].replace('.git','')
    elif 'code.connected' in git_url: 
        department = git_url.split('/')[3].replace('.git','')  if 'http' in git_url else git_url.split(':')[1].split('/')[0].replace('.git','') 
    elif 'github' in git_url: 
        department = git_url.split('/')[3].replace('.git','')  if 'http' in git_url else git_url.split(':')[1].split('/')[0].replace('.git','')

    for build in list_of_builds:
        
        response = requests.get(f'{job_url}/{build}/api/json', 
                                auth=(username, password),
                                headers={jenkins_crumb['crumbRequestField'] : jenkins_crumb['crumb']}).json()
        
        ##Get the job timestamp
        timestamp = int(str(response['timestamp'])[:10])
        timestamp_human_readable = datetime.fromtimestamp(timestamp).isoformat()
        
        for action in response['actions']:
            if 'causes' in action:
                author = action['causes'][0]['userName']  
        duration = response['duration'] / 1000 #ms to seconds transformation
        result = response['result'] 


        #app = git_url.split('/')[4] if git_url.find('https') else git_url.split('/')[5]

        pprint(f"department: {department}")
        payload = {
            'url' : job_url,
            'build' : build,
            'author' : author,
            'git_url' : git_url,
            'timestamp': timestamp_human_readable,
            'build_duration': f"{duration} seconds",
            'isFailed' : result, 
            'department' : department, 
            #'app_name' : app
        }

        
        job_results[job_name + '_' + timestamp_human_readable] = payload

        
    pprint(response)
    return job_results


if __name__ == '__main__':
    print(get_scm_info_from_latest_successful_build())




# TESTS
#get_joburl_and_name = [z for z in server.get_jobs_info()]
    print('checking the job for tests/warning')
    pprint(get_build_info('http://localhost:8080/job/tests/job/warning', 'tests/warning', [10,9,8], 'none'))