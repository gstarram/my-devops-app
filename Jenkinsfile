pipeline {
    agent any

    environment {
        // Replace 'gstarram' with your actual Docker Hub username if different
        DOCKER_USER = 'gstarram'
        APP_NAME = 'devops-app'
        IMAGE_TAG = "v${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout & Test') {
            steps {
                echo 'Testing Python app syntax...'
                sh 'python3 -m py_compile app.py'
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                echo "Building and pushing Docker image: ${DOCKER_USER}/${APP_NAME}:${IMAGE_TAG}"
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
                    sh 'echo $DH_PASS | docker login -u $DH_USER --password-stdin'
                    sh "docker build -t ${DOCKER_USER}/${APP_NAME}:${IMAGE_TAG} ."
                    sh "docker tag ${DOCKER_USER}/${APP_NAME}:${IMAGE_TAG} ${DOCKER_USER}/${APP_NAME}:latest"
                    sh "docker push ${DOCKER_USER}/${APP_NAME}:${IMAGE_TAG}"
                    sh "docker push ${DOCKER_USER}/${APP_NAME}:latest"
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Applying Kubernetes manifests..."
                sh "kubectl apply -f deployment.yaml"
                sh "kubectl rollout restart deployment/devops-app"
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline run failed. Check logs above.'
        }
    }
}
