pipeline {
    agent any

    environment {
        // Указываем путь к установленной версии Python
        PYTHON_HOME = 'C:/Users/sumick/AppData/Local/Programs/Python/Python313'  // Замените на правильный путь к Python 3.13 в Jenkins
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
                    // Установка зависимостей с помощью pip
                    bat 'python -m pip install --upgrade pip'  // Обновление pip
                    bat 'python -m pip install -r requirements.txt'  // Установка зависимостей из requirements.txt
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск юніт-тестів
                    bat 'python -m unittest discover -s tests'  // Запускаем тесты из папки "tests"
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
