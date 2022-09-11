import javaposse.jobdsl.dsl.*
import  javaposse.jobdsl.plugin.*

JenkinsJobManagement jm = new JenkinsJobManagement(System.out, [:], new File('.'));
DslScriptLoader dslScriptLoader = new DslScriptLoader(jm)
dslScriptLoader.runScript("""
freeStyleJob('SEED-JOB-Groovy-Scripted') {
          scm {
              github('ghebu/MariusLaboratory', 'main')
          }
          
          steps {
            dsl {
              external('Jenkins/JenkinsDockerfile/DSL/*.groovy')
              ignoreExisting(true)
              lookupStrategy("JENKINS_ROOT")
              removeViewAction("DELETE")
              removeAction("DELETE")
            }
          }
      }
""".stripIndent().trim())
