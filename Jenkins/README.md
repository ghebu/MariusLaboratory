## SCOPE 

Installing a customised Jenkins for sandbox purposes.


### Deploy
```
docker-compose build --no-cache
docker-compose -up -d 
```

### Fresh deploy 
```
docker-compose down 
docker volume rm jenkins_jenkins_home
docker-compose build --no-cache
docker-compose up -d 
```


### Features 
1. Installing custom Jenkins plugins on [Docker build](JenkinsDockerfile/Jenkins.Dockerfile) by editing the [plugins.txt file](JenkinsDockerfile/scripts/plugins.txt).
    - Passwords can be set from the [Jenkins.Dockerfile](JenkinsDockerfile/Jenkins.Dockerfile) and/or from [docker-compose.yml](docker-compose.yml)

2. Adding configuration as code plugin & [config file](JenkinsDockerfile/scripts/casc-jenkins.yml). [Docs](https://plugins.jenkins.io/configuration-as-code/#plugin-content-getting-started)



### TODO
- [ ] Script auto approvals for seed job
- [ ] As an alternative solution to casc, create groovy script to create the seed job