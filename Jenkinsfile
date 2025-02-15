pipeline {
    agent any
    environment {
        IMAGE_NAME = "sriranjani2809/flask-jenkins-docker"
        CONTAINER_NAME = "flask-app"
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sriranjani2004/flask-jenkins-cicd'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:latest ."
            }
        }
        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', 
                    usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin"
                }
            }
        }
        stage('Push to Registry') {
            steps {
                sh "docker push ${IMAGE_NAME}:latest"
            }
        }
        stage('Run Docker Container') {
            steps {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
                sh "docker run -d -p 5055:5055 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest"
            }
        }
        stage('Clean Up') {
            steps {
                sh "docker image prune -f"
                sh "docker container prune -f"
            }
        }
    }
    post {
        always {
            sh "docker ps -a"
        }
    }
}
