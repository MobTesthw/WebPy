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
				
				//Delete previos vesrsion and create space for new
				ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
					rm -rf ~/Server-Deployment/WebPy/_Current
					mkdir  ~/Server-Deployment/WebPy/_Current
				"
                
                sshagent(['deploy-key']) {
                    sh '''
						#Copy all the files from GitHub to Deployment server:
						scp -r -o StrictHostKeyChecking=no * user@192.168.43.22:~/Server-Deployment/WebPy/
						
                        ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                            # Вывод списка файлов и директорий
                            ls
                            docker images
							docker ps
                            docker-compose up -d
                        "
                    '''
                }
				
				
				


			}
        }
    }
}
