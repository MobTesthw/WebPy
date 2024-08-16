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
				ls
				hostnamectl
                sshagent(['deploy-key']) {
					#echo on root
					ls
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
						ls
						#docker pull webpyflask_web:latest;
						#docker pull webpyflask_python-script:latest;
                        #docker-compose down;
                        #docker-compose up -d"
                    '''
                }
            }
        }
    }
}
