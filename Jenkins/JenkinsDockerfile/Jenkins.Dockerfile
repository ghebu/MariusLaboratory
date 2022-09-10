FROM jenkins/jenkins:2.361.1-lts

ENV CASC_JENKINS_CONFIG=$JENKINS_HOME/casc_configs/
## Installing packages as root
USER 0 
RUN apt update -y && apt install vim curl telnet -y
COPY scripts/install-plugins.sh /usr/local/bin/install-plugins.sh
COPY scripts/plugins.txt /tmp/plugins.txt
COPY groovy/*.groovy $JENKINS_HOME/init.groovy.d/
COPY scripts/casc-jenkins.yml $JENKINS_HOME/casc_configs/jenkins.yaml
RUN chown 1000 /usr/local/bin/install-plugins.sh && \
    chmod +x /usr/local/bin/install-plugins.sh
RUN pluginsList=$(cat /tmp/plugins.txt | grep -vi '^#') && \
    install-plugins.sh $pluginsList
RUN mkdir -p $JENKINS_HOME/{init.groovy.d,casc_configs}
RUN chown -R jenkins.jenkins $JENKINS_HOME/casc_configs $JENKINS_HOME/init.groovy.d


##Switching to Jenkins user
USER 1000
