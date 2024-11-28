pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git credentialsId: 'github-credentials', url: 'https://github.com/sum1ck/Lab1_IT.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Build Executable') {
            steps {
                bat 'python -m PyInstaller --onefile --noconsole --hidden-import PyQt5 --hidden-import numpy --add-data "methods;methods" main.py'
            }
        }

        stage('Archive Build') {
            steps {
                archiveArtifacts artifacts: 'dist/*.exe', fingerprint: true
            }
        }
    }
}
