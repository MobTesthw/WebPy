pipeline {
    agent any
    
    environment {
        PROJECT_NAME = "WebPy"
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '*** Checkout ***'
                git 'https://github.com/MobTesthw/WebPy.git'
            }
        }
        
        stage('Stop and Remove Old Containers and Images') {
            steps {
                script {
                    echo '*** Stop running containers related to the project ***'

                    sshagent(['Server-Deploy-ID']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                                docker-compose -p \"${PROJECT_NAME}\" down --rmi all
                                docker image prune -f
                            "
                        '''


                    }

                    //sh "docker-compose -p \"${PROJECT_NAME}\" down --rmi all"
                    //sh "docker image prune -f"
                }
            }
        }

        stage('Deliver src code to Deploy server') {
            steps {
                script {

                    sshagent(['Server-Deploy-ID']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                                echo '*** Remove previous version and create folder for new code ***'
                                rm -rf ~/Server-Deployment/WebPy/_Current
                                mkdir -p ~/Server-Deployment/WebPy/_Current
                            "
                        '''
                        sh '''
                            echo '*** Copying files to deployment server ***'
                            scp -r -o StrictHostKeyChecking=no * user@192.168.43.22:~/Server-Deployment/WebPy/_Current/
                        '''
                        sh '''
                            ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                                echo '*** Running docker-compose on deployment server ***'
                                ls ~/Server-Deployment/WebPy/_Current
                                cd ~/Server-Deployment/WebPy/_Current
                                docker-compose up -d
                            "
                        '''
                    }
                }
            }
        }

        stage('Build and Deploy New Containers') {
            steps {
                script {
                    //sh "docker-compose -p \"${PROJECT_NAME}\" up --build -d"
                }
            }
        }
    }
    
    post {
        always {
            //sh "docker system prune -f"
        }
    }
}
