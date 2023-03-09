folder('python') { 
  displayName('python-kpi')
  description('DSL jobs for Terraform')
}

pipelineJob('python/python-kpi') {
    displayName('python-kpi')
    description("Capturing job details using the Python Jenkins libraries")

    // parameters {
    //     stringParam("NUM_DAYS_TO_KEEP", "10", "Customize number of days of build history to keep when running this job")
    // }

    definition {
        cpsScm {
            scm{
                git {
                    remote{
                        url("git@github.com:ghebu/MariusLaboratory.git")
                        credentials('github')
                    }
                    branch("*/main")
                }
                scriptPath("Jenkins/jobs/Python/Jenkinsfile")
            }
            lightweight true
        }
    }
}

