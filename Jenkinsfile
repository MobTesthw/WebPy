pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MobTesthw/WebPy.git'
            }
        }

        stage('Empty Stage') {
            steps {
                echo 'This is a placeholder for future tests.'
            }
        }

        stage('Deploy to Docker on Ubuntu') {
            steps {
                sshagent(['deploy-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                        docker pull MobTesthw/webpyapp:web;
                        docker pull MobTesthw/webpyapp:python-script;
                        docker-compose down;
                        docker-compose up -d"
                    '''
                }
            }
        }
    }
}
