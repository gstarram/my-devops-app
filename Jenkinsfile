pipeline {
    agent any

    environment {
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

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${APP_NAME}:${IMAGE_TAG}"
                sh "docker build -t ${APP_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${APP_NAME}:${IMAGE_TAG} ${APP_NAME}:latest"
            }
        }

        stage('Deploy to k3d Kubernetes') {
            steps {
                echo "Importing image into k3d cluster..."
                sh "k3d image import ${APP_NAME}:latest -c mycluster"
                echo "Applying Kubernetes manifests..."
                sh "kubectl apply -f deployment.yaml"
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
