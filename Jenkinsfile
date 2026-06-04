pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo 'Checking python syntax...'
                sh 'python3 -m py_compile app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t heart-app .'
            }
        }
        stage('Deploy Container') {
            steps {
                echo 'Deploying to Docker Desktop...'
                sh 'docker rm -f heart-container || true'
                sh 'docker run -d -p 5000:5000 --name heart-container heart-app'
            }
        }
    }
}
