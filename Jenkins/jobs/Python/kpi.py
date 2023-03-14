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
    return jobs

def get_department(git_url):
    department = ''

    if git_url is None: 
        return department

    if 'bitbucket' in git_url: 
        department = git_url.split('/')[3].replace('.git','')  if 'http' in git_url else git_url.split('/')[5].replace('.git','')
    elif 'code.connected' in git_url: 
        department = git_url.split('/')[3].replace('.git','')  if 'http' in git_url else git_url.split(':')[1].split('/')[0].replace('.git','') 
    elif 'github' in git_url: 
        department = git_url.split('/')[3].replace('.git','')  if 'http' in git_url else git_url.split(':')[1].split('/')[0].replace('.git','')

    return department

def get_author(response):
    
    '''
    Trying to find out the userName in the first list and to return it, if false then cycle through the response actions.
    '''
    if 'causes' in response['action'][0]: 
        author = response['actions'][0]['causes'][0]['userName']
        return author
    
    for action in response['actions']:
        if 'causes' in action:
            author = action['causes'][0]['userName']  
    
    return author

def get_scm_info_from_latest_successful_build(short_job_name):
    build = server[short_job_name]
    
    try:
        git_url = build.get_last_build()._get_git_repo_url()  
    except Exception as e: 
        git_url = None 

    return git_url   

       

def get_build_info(job_url, job_name, list_of_builds, git_url, department):
    
    job_results = {}



    for build in list_of_builds:
        
        response = requests.get(f'{job_url}/{build}/api/json', 
                                auth=(username, password),
                                headers={jenkins_crumb['crumbRequestField'] : jenkins_crumb['crumb']}).json()
        
        ##Get the job timestamp
        timestamp = int(str(response['timestamp'])[:10])
        timestamp_human_readable = datetime.fromtimestamp(timestamp).isoformat()
        
        author = get_author(response)
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
            'result' : result, 
            'department' : department, 
            #'app_name' : app
        }

        
        job_results[job_name + '_' + timestamp_human_readable] = payload

        
    return job_results



def main(): 
    jobs = get_jobs()
    

    pprint(jobs)
    for job in jobs:
        try: 
            short_job_name = job[1]
            build = server[short_job_name]
            list_of_builds = [b for b in build.get_build_ids()]   ##The method doesn't work for some of the builds
            job_url =job[0]

            git_url = get_scm_info_from_latest_successful_build(short_job_name)
            department = get_department(git_url)


            

            print(f"The job {short_job_name} has the builds {list_of_builds}. ")
            print(f"requirements for get_build_info: {job_url}, {short_job_name}, {list_of_builds}, {git_url}, {department}")
            pprint(get_build_info(job_url, short_job_name, list_of_builds, git_url, department))
            

        
        except Exception as e:
            continue 

if __name__ == '__main__':
    pprint(main())

    #pprint(get_build_info('http://localhost:8080/job/tests/job/warning', 'tests/warning', [10,9,8], 'none', ''))


# TESTS
#get_joburl_and_name = [z for z in server.get_jobs_info()]
   