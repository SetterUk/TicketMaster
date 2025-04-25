pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.13.2'
        DJANGO_SETTINGS_MODULE = 'ticket_booking_system.settings'
        VIRTUAL_ENV = "${WORKSPACE}\\venv"
        DOCKER_IMAGE = 'ticketmaster'
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKER_COMPOSE = 'docker-compose'
        PYTHON_HOME = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Python\\Python313"
        PATH = "${PYTHON_HOME};${PYTHON_HOME}\\Scripts;${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Verify Python') {
            steps {
                bat """
                    echo "Checking Python installation..."
                    echo "Python Home: %PYTHON_HOME%"
                    "%PYTHON_HOME%\\python.exe" --version
                    "%PYTHON_HOME%\\python.exe" -m pip --version
                """
            }
        }
        
        stage('Setup Python Environment') {
            steps {
                bat """
                    echo "Creating Virtual Environment..."
                    if exist "%VIRTUAL_ENV%" rmdir /s /q "%VIRTUAL_ENV%"
                    "%PYTHON_HOME%\\python.exe" -m venv "%VIRTUAL_ENV%"
                    call "%VIRTUAL_ENV%\\Scripts\\activate.bat"
                    "%VIRTUAL_ENV%\\Scripts\\python.exe" -m pip install --upgrade pip
                    "%VIRTUAL_ENV%\\Scripts\\pip.exe" install -r requirements.txt
                """
            }
        }
        
        stage('Run Tests') {
            steps {
                bat """
                    call "%VIRTUAL_ENV%\\Scripts\\activate.bat"
                    "%VIRTUAL_ENV%\\Scripts\\python.exe" manage.py test
                """
            }
        }
        
        stage('Security Checks') {
            steps {
                bat """
                    call "%VIRTUAL_ENV%\\Scripts\\activate.bat"
                    "%VIRTUAL_ENV%\\Scripts\\pip.exe" install bandit
                    "%VIRTUAL_ENV%\\Scripts\\bandit.exe" -r .
                """
            }
        }
        
        stage('Build Docker Image') {
            steps {
                bat """
                    docker build -t ticket-booking:%BUILD_NUMBER% .
                """
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'staging'
            }
            steps {
                bat """
                    docker-compose -f docker-compose.staging.yml up -d
                """
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                bat """
                    docker-compose -f docker-compose.prod.yml up -d
                """
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
