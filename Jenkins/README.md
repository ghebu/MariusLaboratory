## SCOPE 

Installing a customised Jenkins for sandbox purposes.


### Deploy
```
docker-compose -up -d 
```

*However if changes are added to the JenkinsDockerfile/Jenkins.Dockerfile file then the command below needs to be ran before:*

```
docker-compose build --no-cache
```


### Features 
1. Installing custom Jenkins plugins on [Docker build](JenkinsDockerfile/Jenkins.Dockerfile) by editing the [plugins.txt file](JenkinsDockerfile/scripts/plugins.txt).
    - Passwords can be set from the [Jenkins.Dockerfile](JenkinsDockerfile/Jenkins.Dockerfile) and/or from [docker-compose.yml](docker-compose.yml)

2. Adding configuration as service plugin & [config file](JenkinsDockerfile/scripts/casc-jenkins.yml). [Docs](https://plugins.jenkins.io/configuration-as-code/#plugin-content-getting-started)



###TODO
[] Script auto approvals for seed job