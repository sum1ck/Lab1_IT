pipeline {
    agent any

    environment {
        PYTHON_HOME = 'C:/Users/sumick/AppData/Local/Programs/Python/Python313'
        PATH = "${PYTHON_HOME}/Scripts;${PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Клонирование репозитория
                git credentialsId: 'github-credentials', url: 'https://github.com/sum1ck/Lab1_IT.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install --upgrade pip'
                    bat 'python -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    bat 'python -m unittest discover -s tests'
                }
            }
        }

        stage('Build Executable') {
            steps {
                script {
                    bat 'python -m PyInstaller --onefile --noconsole --hidden-import PyQt5 --hidden-import numpy --add-data "methods;methods" main.py'
                }
            }
        }

        stage('Archive Build') {
            steps {
                archiveArtifacts artifacts: 'dist/*.exe', fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
