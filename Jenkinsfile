pipeline {
    agent any
    environment {
        VENV = 'venv'
        IMAGE_NAME = 'heart-app'
        CONTAINER_NAME = 'heart-container'
    }
    stages {
        stage('Checkout Out') {
            steps {
                checkout scm
            }
        }
        stage('Set up VENV') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/python -m pip install --upgrade pip'
                sh 'venv/bin/python -m pip install -r requirements.txt'
            }
        }
        stage('Run the tests') {
            steps {
                echo 'Checking python syntax...'
                sh 'venv/bin/python -m py_compile app.py'
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker Image...'
                sh "docker build -t ${IMAGE_NAME} ."
            }
        }
        stage('Deploy Container') {
            steps {
                echo 'Deploying to Docker Desktop...'
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
            }
        }
    }
}
