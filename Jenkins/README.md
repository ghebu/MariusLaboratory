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
1. Installing the necessary plugins on [Docker build](JenkinsDockerfile/Jenkins.Dockerfile) by editing the [plugins.txt file](JenkinsDockerfile/plugins.txt). 