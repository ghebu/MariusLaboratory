//DOCS 
/*
https://github.com/jenkinsci/build-failure-analyzer-plugin/blob/master/src/test/java/com/sonyericsson/jenkins/plugins/bfa/PluginImplHudsonTest.java
https://javadoc.jenkins.io/plugin/build-failure-analyzer/com/sonyericsson/jenkins/plugins/bfa/package-summary.html
*/

//package com.sonyericsson.jenkins.plugins.bfa
import com.sonyericsson.jenkins.plugins.bfa.*;
import hudson.util.Secret;
import com.sonyericsson.jenkins.plugins.bfa.db.MongoDBKnowledgeBase;
import com.sonyericsson.jenkins.plugins.bfa.db.KnowledgeBase;
import com.sonyericsson.jenkins.plugins.bfa.db.LocalFileKnowledgeBase;
import com.sonyericsson.jenkins.plugins.bfa.db.MongoDBKnowledgeBase;



PluginImpl bfa = new PluginImpl(); 
PluginImpl instance = PluginImpl.getInstance();


def host = "mongo"
def dbName = "jenkins"
def userName = null ?: "ghebu"
def password = null ?: "passw0rd"
boolean updateMongoConfiguration = false;
boolean foundLocalFile = false;
boolean foundMongoDB = false;
boolean configuredMongoDB = false;
/*
public MongoDBKnowledgeBase(String host,
                            int port,
                            String dbName,
                            String userName,
                            Secret password,
                            boolean enableStatistics,
                            boolean successfulLogging)
*/


def kdbDescriptor = bfa.getKnowledgeBaseDescriptor("MongoDBKnowledgeBaseDescriptor");
def kdb = bfa.getKnowledgeBase();
println(kdb)

ExtensionList<KnowledgeBase.KnowledgeBaseDescriptor> descriptors =
                PluginImpl.getInstance().getKnowledgeBaseDescriptors();


for (KnowledgeBase.KnowledgeBaseDescriptor descriptor : descriptors) {
    if (descriptor instanceof LocalFileKnowledgeBase.LocalFileKnowledgeBaseDescriptor) {
        foundLocalFile = true;
    } else if (descriptor instanceof MongoDBKnowledgeBase.MongoDBKnowledgeBaseDescriptor) {
        foundMongoDB = true;
        mongoDescriptor = descriptor
    } 
}

if ((kdbDescriptor == mongoDescriptor) && !updateMongoConfiguration) {
	mongoKdb = true
    println(mongoKdb)
} else {
    MongoDBKnowledgeBase mongoKB = new MongoDBKnowledgeBase(host,27017, dbName, userName, Secret.fromString("passw0rd"), true, true);
    instance.setKnowledgeBase(mongoKB);
    instance.save();
} 

