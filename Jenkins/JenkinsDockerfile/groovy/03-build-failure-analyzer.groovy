
//Docs 
/*
https://github.com/jenkinsci/build-failure-analyzer-plugin/blob/master/src/test/java/com/sonyericsson/jenkins/plugins/bfa/PluginImplHudsonTest.java
https://javadoc.jenkins.io/plugin/build-failure-analyzer/com/sonyericsson/jenkins/plugins/bfa/package-summary.html
*/

import com.sonyericsson.jenkins.plugins.bfa.*
//package com.sonyericsson.jenkins.plugins.bfa
  
PluginImpl bfa = new PluginImpl();

println("Is globally enabled: " + bfa.isGlobalEnabled());
bfa.setGlobalEnabled(true);
println("Is globally enabled: " + bfa.isGlobalEnabled());
println("Is instance: " + bfa.isInstance());

bfa.setMaxLogSize(bfa.DEFAULT_MAX_LOG_SIZE);
bfa.save();

println(bfa.DEFAULT_MAX_LOG_SIZE)
println("Max log size is: " + bfa.getMaxLogSize())


def knownDatabaseDescriptor = bfa.getKnowledgeBaseDescriptors().findAll { s -> s ==~ /.*Mongo.*/ }[0]
println(knownDatabaseDescriptor)

bfa.setKnowledgeBase(knownDatabaseDescriptor)

