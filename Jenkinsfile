pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                url: 'https://github.com/Mohd-kaif123/python_CI.git'
            }
        }
        stage('Check Python version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Create Virtual Environment') {
            steps {
                sh 'python3 -m venv venv'
            }
        }
        stage('Install Dependensies') {
            steps {
                sh '''
                . venv/bin/activate
                pip install --upgrade pip
                pip install - requiremnts.txt
                '''
            }
        }
        stage('Run Test Cases') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                ...

            }
    }
}

post {
    success {
        echo 'Calculator CI Pipeline Successful!'
        }
        failure {
            echo 'Pipeline Failed!'
        }
    }
}