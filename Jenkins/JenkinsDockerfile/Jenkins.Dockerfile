FROM jenkins/jenkins:2.361.1-lts

ENV CASC_JENKINS_CONFIG=$JENKINS_HOME/casc_configs/
## Installing packages as root
USER 0 

## Updating the packages
RUN apt update -y && apt install vim curl telnet -y

## Copy utilitarians
COPY scripts/plugins.txt /tmp/plugins.txt
COPY groovy/*.groovy $JENKINS_HOME/init.groovy.d/
COPY scripts/casc-jenkins.yml $JENKINS_HOME/casc_configs/jenkins.yaml

## Installing the plugins from /scripts/plugins.txt using the built-in jenkins-plugin-cli script
RUN pluginsList=$(cat /tmp/plugins.txt | grep -vi '^#' | tr "\n" " ") && \
    /bin/jenkins-plugin-cli -p $pluginsList

## Configuration-as-code & groovy init folder creation
RUN mkdir -p $JENKINS_HOME/{init.groovy.d,casc_configs}
RUN chown -R jenkins.jenkins $JENKINS_HOME/casc_configs $JENKINS_HOME/init.groovy.d


##Switching to Jenkins user
USER 1000
