// //https://www.happycoders.eu/devops/jenkins-tutorial-implementing-seed-job/
// import javaposse.jobdsl.dsl.*
// import  javaposse.jobdsl.plugin.*

// // Disabling script security for JobDSL
// GlobalConfiguration.all().get(GlobalJobDslSecurityConfiguration).configure(null, new JSONObject())

// def jobDsl = '''
// job {
//     name 'hello-world'
//     steps {
//         shell('echo "Hello World!"')
//     }
// }
// '''

// def JenkinsJobManagement jm = new JenkinsJobManagement(System.out, [:], new File('.'));  
// new DslScriptLoader dslScriptLoader = new DslScriptLoader(jm)
// dslScriptLoader.runScript(jobDsl)




// //https://github.com/jenkinsci/job-dsl-plugin/wiki/Testing-DSL-Scripts
// import groovy.util.FileNameFinder
// import javaposse.jobdsl.dsl.DslScriptLoader
// import javaposse.jobdsl.plugin.JenkinsJobManagement
// import org.junit.ClassRule
// import org.jvnet.hudson.test.JenkinsRule
// import spock.lang.Shared
// import spock.lang.Specification
// import spock.lang.Unroll

// class JobScriptsSpec extends Specification {
//     @Shared
//     @ClassRule
//     JenkinsRule jenkinsRule = new JenkinsRule()

//     @Unroll
//     def 'test script #file.name'(File file) {
//         given:
//         def jobManagement = new JenkinsJobManagement(System.out, [:], new File('.'))

//         when:
//         new DslScriptLoader(jobManagement).runScript(file.text)

//         then:
//         noExceptionThrown()

//         where:
//         file << new FileNameFinder().getFileNames('jobs', '**/*.groovy').collect { new File(it) }
//     }
// }
