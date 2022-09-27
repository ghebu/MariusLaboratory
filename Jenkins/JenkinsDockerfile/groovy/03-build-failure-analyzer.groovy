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
import java.util.regex.*
import com.sonyericsson.jenkins.plugins.bfa.model.FailureCause;
import com.sonyericsson.jenkins.plugins.bfa.model.indication.BuildLogIndication;



PluginImpl bfa = new PluginImpl(); 
PluginImpl instance = PluginImpl.getInstance();



def host = "mongo";
def dbName = "jenkins";
def userName = null ?: "ghebu";
def password = null ?: "passw0rd";
def port = 27017;
boolean enableStatistics = false;
boolean successfulLogging = true;

boolean updateMongoConfiguration = true;
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

def isMongoConfigured = kdb ==~ /.*MongoDBKnowledgeBase.*/

ExtensionList<KnowledgeBase.KnowledgeBaseDescriptor> descriptors =
                PluginImpl.getInstance().getKnowledgeBaseDescriptors();

for (KnowledgeBase.KnowledgeBaseDescriptor descriptor : descriptors) {
    if (descriptor instanceof LocalFileKnowledgeBase.LocalFileKnowledgeBaseDescriptor) {
        foundLocalFile = true;
    } else if (descriptor instanceof MongoDBKnowledgeBase.MongoDBKnowledgeBaseDescriptor) {
        foundMongoDB = true;
        mongoDescriptor = descriptor;
        
        testConnection = descriptor.doTestConnection(host, port, dbName, userName, password,false,true);
        //println(testConnection)  //Should return --> OK: Connection OK!
        mongoConnected = testConnection ==~ /OK: Connection OK!/ //returns boolean value if the connectin to the Mongo DB is successful or not.
        println("Is the connection to Mongo DB successful?: " + mongoConnected)

    } 
}

if (isMongoConfigured && !updateMongoConfiguration && mongoConnected) {
	mongoKdb = true;
    println("MongoDB is already configured and it will not be updated.");
} else if (updateMongoConfiguration && mongoConnected){ 
    //MongoDBKnowledgeBase(String host, int port, String dbName, String userName, Secret password, boolean enableStatistics, boolean successfulLogging)
    MongoDBKnowledgeBase mongoKB = new MongoDBKnowledgeBase(host, port, dbName, userName, Secret.fromString("passw0rd"), enableStatistics, successfulLogging);
    instance.setKnowledgeBase(mongoKB);
    instance.save();
    println("MongoDB was configured as " + kdb);
} else { 
    println("Cannot update the knowledge base. Mongo is not configured and there is no connection to the specified MongoDB")
}





if(isMongoConfigured && mongoConnected) {
    //Defining Cause
    def causeName = "IsADirectory"
    def causeDescription = "Checking if the file is a directory or not"
    def causeComment = "You are trying to read a directory instead of a file"
    def causeCategory = "BASH"
    def causeLogFilter = "cat: .*: Is a directory"

    //FailureCause(String name, String description, String comment, String categories)

    FailureCause cause = new FailureCause(causeName, causeDescription, causeComment, causeCategory );
    cause.addIndication(new BuildLogIndication(causeLogFilter));
    cause = kdb.addCause(cause);
    println("A new Failure Cause created")
}


