pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-python-app"
        // Make sure your DISPLAY environment variable is set on your Jenkins agent host.
        // For example, if you're logged into a desktop session on your VM, it might be :0
        DISPLAY_VAR = "${env.DISPLAY ?: ':0'}"
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
                    // Build the Docker image. The tag is based on the build ID.
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }
        stage('Run Container (with X11 Forwarding)') {
            steps {
                script {
                    echo "Running container with GUI support..."
                    // Using dockerImage.inside with additional docker run arguments.
                    // Here we pass the DISPLAY variable and mount the X11 socket.
                    dockerImage.inside("-e DISPLAY=${DISPLAY_VAR} -v /tmp/.X11-unix:/tmp/.X11-unix") {
                        // Run the Python script inside the container.
                        // Your Dockerfile's CMD may already do this, but here we're explicitly calling it.
                        sh 'python script.py'
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
    }
}

