pipeline {
    agent any

    environment {
        VENV_PATH = 'venv' // Define virtual environment path
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', 'https://github.com/caioaza/Testing_OpenCart_Project'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh 'python -m venv $VENV_PATH'
                sh 'source $VENV_PATH/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'behave OpenCartDemoSimulation/features/login.feature -f allure_behave.formatter:AllureFormatter -o reports/allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    results: [[path: 'reports/allure-results']]
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/allure-results/**', fingerprint: true
            junit 'reports/allure-results/*.xml'
        }
    }
}
