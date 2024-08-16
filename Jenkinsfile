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
                echo "Starting deployment"
                sh 'ls' // Вывод содержимого текущей директории
                //sh 'hostnamectl' // Вывод информации о хосте
                
                sshagent(['deploy-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                            # Вывод списка файлов и директорий
                            ls
                            docker images
							docker ps
                            ## Команды для управления Docker
                            #docker pull webpyflask_web:latest
                            #docker pull webpyflask_python-script:latest
                            #docker-compose down
                            #docker-compose up -d
                        "
                    '''
                }


			}
        }
    }
}
