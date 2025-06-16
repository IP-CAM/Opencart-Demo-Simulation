pipeline {
    agent any

    environment {
        PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv %PYTHON_ENV%
                call %PYTHON_ENV%\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat '''
                call %PYTHON_ENV%\\Scripts\\activate
                set PYTHONPATH=%CD%
                pytest --maxfail=1 --disable-warnings --junitxml=test-results/results.xml
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                call %PYTHON_ENV%\\Scripts\\activate
                allure generate ./allure-results --clean -o ./allure-report
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/results.xml', allowEmptyArchive: true
            junit 'test-results/results.xml'
        }
    }
}
