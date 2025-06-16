pipeline {
    agent any

    environment {
        PYTHON_ENV = "venv"
        PYTHONPATH = "${env.WORKSPACE}\\OpenCartDemoSimulation"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/caioaza/OpenCartDemoSimulation.git'
            }
        }

        stage('Rebuild folder structure for imports') {
            steps {
                bat '''
                mkdir OpenCartDemoSimulation
                xcopy /E /I /Y pageObjects OpenCartDemoSimulation\\pageObjects
                xcopy /E /I /Y utilities OpenCartDemoSimulation\\utilities
                xcopy /E /I /Y tests OpenCartDemoSimulation\\tests
                copy requirements.txt OpenCartDemoSimulation\\
                copy __init__.py OpenCartDemoSimulation\\
                '''
            }
        }

        stage('Setup Python Environment') {
            steps {
                dir('OpenCartDemoSimulation') {
                    bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Selenium Tests') {
            steps {
                dir('OpenCartDemoSimulation') {
                    bat '''
                    call venv\\Scripts\\activate
                    set PYTHONPATH=%CD%
                    pytest --maxfail=1 --disable-warnings --junitxml=../test-results/results.xml --html=reports\\report.html --self-contained-html
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                dir('OpenCartDemoSimulation') {
                    bat '''
                    call venv\\Scripts\\activate
                    allure generate ./allure-results --clean -o ./allure-report
                    '''
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/report.html', allowEmptyArchive: true
            archiveArtifacts artifacts: '**/results.xml', allowEmptyArchive: true
            junit 'test-results/results.xml'
        }
    }
}
