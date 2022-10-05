folder('noaptea-companiilor') { 
  displayName('noaptea-companiilor')
  description('DSL jobs for Terraform')
}

pipelineJob('noaptea-companiilor/terraform') {
    displayName('Terraform')
    description("Showcasing TF and Jenkins for Noaptea Companiilor event")

    // parameters {
    //     stringParam("NUM_DAYS_TO_KEEP", "10", "Customize number of days of build history to keep when running this job")
    // }

    definition {
        cpsScm {
            scm{
                git {
                    remote{
                        url("https://github.com/ghebu/noaptea-companiilor22")
                    }
                    branch("*/main")
                }
                scriptPath("terraform/Jenkinsfile")
            }
            lightweight true
        }
    }
}