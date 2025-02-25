pipeline {
    agent any

    environment {
        // Repository information for Docker Hub
        DOCKER_HUB_REPO = "myousufhasnain/docker-practice"
        // Tag image using the Jenkins BUILD_ID; you can also use a fixed tag like "tagname"
        IMAGE_TAG = "${env.BUILD_ID}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code from GitHub..."
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    // Build the Docker image using your Dockerfile
                    dockerImage = docker.build("${DOCKER_HUB_REPO}:${IMAGE_TAG}")
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image to Docker Hub..."
                    // Log in to Docker Hub using the stored credentials, then push image
                    docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                        dockerImage.push("${IMAGE_TAG}")
                        dockerImage.push("latest")
                    }
                }
            }
        }
        stage('Deploy') {
            when {
                branch 'main'  // Only deploy on the main branch
            }
            steps {
                script {
                    echo "Deploying Docker container..."
                    // This stage simulates deployment.
                    // For example, stop an old container and run the new image.
                    sh """
                      docker stop docker-practice-container || true
                      docker run --rm -d --name docker-practice-container -p 8050:8050 ${DOCKER_HUB_REPO}:${IMAGE_TAG}
                    """
                }
            }
        }
    }
    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the logs."
            // Optionally, add rollback logic here (e.g., redeploy the image tagged "latest")
        }
    }
}

