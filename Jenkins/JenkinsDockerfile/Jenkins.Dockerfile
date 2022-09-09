FROM jenkins/jenkins:2.361.1-lts

## Installing packages as root
USER 0 
RUN apt update -y && apt install vim curl telnet -y
COPY install-plugins.sh /usr/local/bin/install-plugins.sh
RUN chown 1000 /usr/local/bin/install-plugins.sh && \
    chmod +x /usr/local/bin/install-plugins.sh


##Switching to Jenkins user
USER 1000
COPY plugins.txt /tmp/plugins.txt
RUN pluginsList=$(cat /tmp/plugins.txt | grep -vi '^#') && \
    install-plugins.sh $pluginsList