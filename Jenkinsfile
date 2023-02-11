pipeline{
    agent { label 'jenkins-agent' }
    stages{
        stage("sonarqube"){
            steps{
            
            script{
            def pipelineconfig=[
                sonarQubeServer:'sonarqube-connection',
            ]
            def repositoryUrl = scm.userRemoteconfigs[0].getUrl()
            def GIT_REPO_NAME = scm.userRemoteconfigs[0].getUrl().tokenize.last().split("\\")[0]
            def scannerHome = tool 'sonarqube-global'
            def SONAR_BRANCH_NAME = env.BRANCH_NAME
            withSonarQubeEnv('sonarqube-connection') {
                sh "sed -i s#{{repo_name}}s#{GIT_REPO_NAME}# sonar-project.proberties"
                sh "sed -i s#{{branch_name}}s#{SONAR_BRANCH_NAME}# sonar-project.proberties"
                sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectVersion=${SONAR_BRANCH_NAME} -Dsonar.buildString=Jenkins-${SONAR_BRANCH_NAME}BLD${env.BUILD_NUMBER}"
            }
        }
    }
}
}
}
