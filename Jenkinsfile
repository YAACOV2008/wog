pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = "wog-app"
        DOCKER_TAG = "latest"
        REPO_URL = "https://github.com/YAACOV2008/wog.git"
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the repository
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Build the Docker image using Dockerfile
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    // Run the application detached
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Run the end-to-end test using Selenium
                    sh 'python ./tests/e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    // Terminate the running container and clean up volumes and orphan containers
                    sh 'docker-compose down --volumes --remove-orphans'

                    // Use DockerHub credentials securely from Jenkins credentials store
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials',
                     passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                        sh 'docker login -u $DOCKERHUB_USERNAME -p $DOCKERHUB_PASSWORD'
                        sh 'docker push $DOCKERHUB_USERNAME/$DOCKER_IMAGE_NAME:$DOCKER_TAG'
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }

        failure {
            echo "Pipeline failed, please check the logs!"
        }
    }
}
