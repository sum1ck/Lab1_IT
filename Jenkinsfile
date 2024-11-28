pipeline {
    agent any  // Этот параметр указывает, что пайплайн может быть выполнен на любом доступном агенте

    tools {
        python 'Python 3.13'  // Устанавливаем нужную версию Python, которая настроена в Jenkins
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
                    // Установка зависимостей с помощью pip
                    bat 'python -m pip install --upgrade pip'  // Обновление pip
                    bat 'python -m pip install -r requirements.txt'  // Установка зависимостей из requirements.txt
                }
            }
        }

        stage('Build Executable') {
            steps {
                script {
                    // Создание исполняемого файла с помощью PyInstaller
                    bat 'python -m PyInstaller --onefile --noconsole --hidden-import PyQt5 --hidden-import numpy --add-data "methods;methods" main.py'
                }
            }
        }

        stage('Archive Build') {
            steps {
                // Архивирование собранного исполняемого файла
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
