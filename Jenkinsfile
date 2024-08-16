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
                sh 'ls' // List the contents of the current directory
                // sh 'hostnamectl' // Display host information (commented out)

                sshagent(['deploy-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                            # Remove previous version and create space for new
                            rm -rf ~/Server-Deployment/WebPy/_Current
                            mkdir -p ~/Server-Deployment/WebPy/_Current
                        "

                        # Copy all files from the current workspace to the Deployment server
                        scp -r -o StrictHostKeyChecking=no * user@192.168.43.22:~/Server-Deployment/WebPy/_Current/

                        ssh -o StrictHostKeyChecking=no user@192.168.43.22 "
                            # List files and directories
                            ls ~/Server-Deployment/WebPy/_Current
                            
                            # Pull Docker images, if necessary
                            docker images
                            
                            # Run Docker Compose
                            cd ~/Server-Deployment/WebPy/_Current
                            docker-compose up -d
                        "
                    '''
                }
            }
        }
    }
}
