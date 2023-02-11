pipeline{
    agent{
        label "Agent slave"
    }
    stages{
        stage("sonarqube"){
            steps{
            }
            script{
            def pipelineconfig=[
                sonarQubeServer:'sonarqube-connection',
            ]
            def repositoryUrl() = scm.userRemoteconfigs[0].getUrl()
            def GIT_REPO_NAME() = scm.userRemoteconfigs[0].getUrl().tokenize.last().split("\\")[0]
            def scannarHome = tools('sonarqube-global')
            def SONAR_BARANCH_NAME = env.BARANCH_NAME
            withSonarQubeEnv('sonarqube-connection') {
                sh "sed -i s#{{repo_name}}s#{GIT_REPO_NAME}# sonar-project.proberties"
                sh "sed -i s#{{baranch_name}}s#{SONAR_BARANCH_NAME}# sonar-project.proberties"
sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectVersion=${SONAR_BARANCH_NAME} -Dsonar.buildString=Jenkins-${SONAR_BARANCH_NAME}BLD${env.BUILD_NUMBER}"
            }
        }
    }
}
}
