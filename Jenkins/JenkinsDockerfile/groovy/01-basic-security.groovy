#!groovy

import jenkins.model.*
import hudson.util.*;
import jenkins.install.*;
import hudson.security.*
import net.sf.json.JSONObject
import jenkins.model.GlobalConfiguration
import javaposse.jobdsl.plugin.GlobalJobDslSecurityConfiguration

def instance = Jenkins.getInstance()
def hudsonRealm = new HudsonPrivateSecurityRealm(false)

def admin_name = System.getenv('ADMIN_USERNAME') ?: 'admin'
def admin_password = System.getenv('ADMIN_PASSWORD') ?: 'passw0rd'


hudsonRealm.createAccount(admin_name,admin_password)
instance.setSecurityRealm(hudsonRealm)

instance.setInstallState(InstallState.INITIAL_SETUP_COMPLETED)
instance.save()

// Disabling script security for JobDSL
GlobalConfiguration.all().get(GlobalJobDslSecurityConfiguration).configure(null, new JSONObject())



