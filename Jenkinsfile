pipeline {
    agent any

    environment {
        IMAGE_NAME = "tic-tac-toe"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out the code..."
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }
        stage('Simulate Game') {
            steps {
                script {
                    echo "Running Tic Tac Toe simulation inside container..."
                    // Simulate a game by piping predefined moves into the Python script.
                    dockerImage.inside {
                        // Note: Adjust the moves if desired. Here they simulate moves for all 9 positions.
                        sh 'echo -e "1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9" | python tic_tac_toe.py'
                    }
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
        }
    }
}

