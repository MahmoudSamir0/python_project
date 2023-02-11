pipeline{
    agent { label 'jenkins-agent' }
    stages{
        stage("sonarqube"){
            steps{
            
            script{
            def pipelineconfig=[
                sonarQubeServer:'sonarqube-connection',
            ]
            def repositoryUrl = scm.userRemoteConfigs[0].getUrl()
            def GIT_REPO_NAME = scm.userRemoteConfigs[0].getUrl().tokenize('/').last().split("\\.")[0]
            def scannerHome = tool 'sonarqube-global'
            def SONAR_BRANCH_NAME = env.BRANCH_NAME
            withSonarQubeEnv('sonarqube-connection') {
                sh "sed -i s#{{repo_name}}#${GIT_REPO_NAME}# sonar-project.proberties"
                sh "sed -i s#{{branch_name}}#${SONAR_BRANCH_NAME}# sonar-project.proberties"
                sh "${scannerHome}/bin/sonar-scanner
            }
        }
    }
}
}
}
