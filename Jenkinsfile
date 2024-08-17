pipeline {
    agent any
    
    environment {
        // Присваиваем имя вашему проекту
        PROJECT_NAME = "WebPy"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Получаем последний код из репозитория
                git 'https://github.com/MobTesthw/WebPy.git'
            }
        }
        
        stage('Stop and Remove Old Containers and Images') {
            steps {
                script {
                    echo '*** Stop running containers related to the poject'
                    // Останавливаем и удаляем все контейнеры с именем проекта
                    sh "docker-compose -p ${PROJECT_NAME} down --rmi all"
                    
                    // Дополнительно удаляем все dangling images (сиротские образы, не привязанные к контейнерам)
                    sh "docker image prune -f"
                }
            }
        }
        stage('Deliver src code to Deploy server') {
            steps {
                script {
                    sshagent(['deploy-key']) {
                        sh '''
                            ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                                echo '*** Remove previous version and create folder for new code'
                                rm -rf ~/Server-Deployment/WebPy/_Current
                                mkdir -p ~/Server-Deployment/WebPy/_Current
                            "

                            # Copy all files from the current workspace to the Deployment server
                            scp -r -o StrictHostKeyChecking=no * user@192.168.43.22:~/Server-Deployment/WebPy/_Current/
                            echo "*************** Printout**********"
                            cat ./web/templates/index.html

                            ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                                # List files and directories
                                ls ~/Server-Deployment/WebPy/_Current
                                
                                # Pull Docker images, if necessary
                                docker images
                                
                                # Run Docker Compose
                                cd ~/Server-Deployment/WebPy/_Current
                                docker-compose up -d
                            "
                    }    '''
                }
            }
        }

        stage('Build and Deploy New Containers') {
            steps {
                script {
                    // Сборка и запуск контейнеров с новым кодом
                    sh "docker-compose -p ${PROJECT_NAME} up --build -d"
                }
            }
        }
    }
    
    post {
        always {
            // Чистка лишних ресурсов после сборки, если необходимо
            sh "docker system prune -f"
        }
    }
}