pipeline {
    agent any
    
    environment {
        GIT_CREDENTIALS_ID = 'GitHub-MobTestHW-ID'
        SSH_CREDENTIALS_ID = 'Server-Deploy-ID'
        DEPLOY_SERVER = 'user@192.168.33.33'
        PROJECT_NAME = 'WebPy'
        REMOTE_DIR = "~/Server-Deployment/${PROJECT_NAME}"
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository from GitHub using the provided credentials
                git credentialsId: "${GIT_CREDENTIALS_ID}", url: 'https://github.com/MobTesthw/WebPy.git'
            }
        }
        
        stage('Stop and Remove Old Containers and Images on Server') {
            steps {
                script {
                    sshagent([SSH_CREDENTIALS_ID]) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no ${DEPLOY_SERVER} "
                                echo '*** Stopping and removing old containers and images ***'
                                cd ${REMOTE_DIR}
                                docker-compose down --rmi all
                                docker image prune -f
                            "
                        '''
                    }
                }
            }
        }
        
        stage('Deliver Source Code to Deploy Server') {
            steps {
                script {
                    sshagent([SSH_CREDENTIALS_ID]) {
                        sh '''
                            echo '*** Creating remote directory on server ***'
                            ssh -o StrictHostKeyChecking=no ${DEPLOY_SERVER} "mkdir -p ${REMOTE_DIR}"

                            echo '*** Copying project files to the deploy server ***'
                            scp -r -o StrictHostKeyChecking=no * ${DEPLOY_SERVER}:${REMOTE_DIR}/
                        '''
                    }
                }
            }
        }

        stage('Deploy New Build on Server') {
            steps {
                script {
                    sshagent([SSH_CREDENTIALS_ID]) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no ${DEPLOY_SERVER} "
                                echo '*** Deploying the new build ***'
                                cd ${REMOTE_DIR}
                                docker-compose up --build -d
                            "
                        '''
                    }
                }
            }
        }
    }
    
    post {
        always {
            script {
                sshagent([SSH_CREDENTIALS_ID]) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ${DEPLOY_SERVER} "
                            echo '*** Cleaning up unused Docker resources ***'
                            docker system prune -f
                        "
                    '''
                }
            }
        }
    }
}
