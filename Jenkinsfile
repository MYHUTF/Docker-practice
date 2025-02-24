pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-python-app"
    }

    stages {
        stage('Checkout') {
            steps {
                // This pulls your code from GitHub
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }
        stage('Run Container') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python script.py'
                    }
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}


