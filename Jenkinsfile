pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'ticketmaster'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        DOCKER_COMPOSE = 'docker-compose'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    python manage.py test
                '''
            }
        }
        
        stage('Code Quality') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install flake8
                    flake8 .
                '''
            }
        }
        
        stage('Security Check') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip install bandit
                    bandit -r .
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                sh '''
                    ${DOCKER_COMPOSE} -f docker-compose.yml up -d
                    ${DOCKER_COMPOSE} exec -T web python manage.py migrate
                    ${DOCKER_COMPOSE} exec -T web python manage.py collectstatic --no-input
                '''
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?'
                sh '''
                    ${DOCKER_COMPOSE} -f docker-compose.prod.yml up -d
                    ${DOCKER_COMPOSE} exec -T web python manage.py migrate
                    ${DOCKER_COMPOSE} exec -T web python manage.py collectstatic --no-input
                '''
            }
        }
    }
    
    post {
        always {
            sh '${DOCKER_COMPOSE} down || true'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
            mail to: 'admin@ticketmaster.com',
                 subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
                 body: "Pipeline failed. Please check: ${env.BUILD_URL}"
        }
    }
}
