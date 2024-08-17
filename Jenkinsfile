pipeline {
    agent any
    
    environment {
        // Присваиваем имя вашему проекту
        PROJECT_NAME = "my_project"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Получаем последний код из репозитория
                git 'https://your-repo-url.git'
            }
        }
        
        stage('Stop and Remove Old Containers and Images') {
            steps {
                script {
                    // Останавливаем и удаляем все контейнеры с именем проекта
                    sh "docker-compose -p ${PROJECT_NAME} down --rmi all"
                    
                    // Дополнительно удаляем все dangling images (сиротские образы, не привязанные к контейнерам)
                    sh "docker image prune -f"
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