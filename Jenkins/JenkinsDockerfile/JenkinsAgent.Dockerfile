#docker run -d --init --network=jenkins_default jenkins/inbound-agent -url http://jenkins:8080 -workDir=/home/jenkins/agent "7c4e2d48de8fb9979c8cc5d1f640a07a7a62357e58eca260bc9f008450c71103" "docker-agent"

FROM jenkins/inbound-agent
USER 0 
RUN apt update -y && apt install jq telnet curl -y 

 
ENV TERRAFORM_VERSION=1.4.0
RUN  apt-get update &&  apt-get install -y gnupg software-properties-common wget curl python3-pip 

# Install terraform using tfswitch
RUN curl -L https://raw.githubusercontent.com/warrensbox/terraform-switcher/release/install.sh | bash
RUN find / -name terraform_${TERRAFORM_VERSION} -print0  | xargs -0 -I {} cp {}  /usr/local/bin/terraform  
RUN pip3 install python-jenkins jenkinsapi    

# Install awscli 
RUN pip install awscli


RUN chown 1000 -R /usr/local/bin/

USER 1000

WORKDIR /home/jenkins/agent
RUN tfswitch $TERRAFORM_VERSION


#RUN export TOKEN="$(curl -L -s -u ghebu:passw0rd  -X GET http://jenkins:8080/computer/docker-agent/slave-agent.jnlp | sed 's/.*<application-desc main-class=\"hudson.remoting.jnlp.Main\"><argument>\([a-z0-9]*\).*/\1/' | grep -E -o '<argument>.*</argument>'  | cut -d '>' -f2 | cut -d '<' -f1)"
ARG TOKEN

ENV JENKINS_SECRET=${TOKEN}   
ENV JENKINS_URL="http://jenkins:8080"
ENV JENKINS_AGENT="docker-agent"


