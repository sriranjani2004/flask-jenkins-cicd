pipeline {
    agent any
    environment {
        IMAGE_NAME = "sriranjani2809/flask-jenkins-docker"
        CONTAINER_NAME = "flask-app"
    }
    tools {
        docker 'Docker'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sriranjani2004/flask-jenkins-cicd'
            }
        }
        stage('Ensure Docker is Available') {
            steps {
                sh '''
                    set -e
                    if ! command -v docker &> /dev/null; then
                        echo "Docker not found, trying to update PATH..."
                        export PATH=$PATH:/usr/local/bin
                        if ! command -v docker &> /dev/null; then
                            echo "Docker still not found. Please install Docker."
                            exit 1
                        fi
                    fi
                    docker --version
                '''
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
                    sh '''
                        set -e
                        echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin
                    '''
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
                sh '''
                    set -e
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d -p 5055:5055 --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest
                '''
            }
        }
        stage('Clean Up') {
            steps {
                sh '''
                    set -e
                    docker image prune -f
                    docker container prune -f
                '''
            }
        }
    }
    post {
        always {
            sh "docker ps -a"
        }
    }
}
