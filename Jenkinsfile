pipeline {
    agent any
    environment {
	VERSION = '$GIT_COMMIT'
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		        sh 'docker build -t "dev/test:$GIT_COMMIT" .' 					
		        echo "BUILD WAS SUCCESSFUL"
		    }
        }
        stage('Push') {
            steps {
                echo 'Pushing to ECR..'
		        sh 'aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 392209090241.dkr.ecr.eu-central-1.amazonaws.com'
		        sh 'docker tag dev/test:$GIT_COMMIT 392209090241.dkr.ecr.eu-central-1.amazonaws.com/dev/test:$GIT_COMMIT'
		        sh 'docker push 392209090241.dkr.ecr.eu-central-1.amazonaws.com/dev/test:$GIT_COMMIT'
            }
        }
        stage('Deploy'){
            steps{
                echo "Deploying locally..."
                sh 'docker pull 392209090241.dkr.ecr.eu-central-1.amazonaws.com/dev/test:$GIT_COMMIT'
                sh 'docker rm --force view-me'
                sh 'docker run -dit --name view-me -p 5000:5000 392209090241.dkr.ecr.eu-central-1.amazonaws.com/dev/test:$GIT_COMMIT'
            }
        }
        stage('Smoke Tests'){
            steps{
                echo "Running simple test"
                sleep 5
                // Use curl to check health and fail the build if the status is not 200
                sh '''
                    status_code=$(curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:5000/health)
                    if [ "$status_code" -ne 200 ]; then
                        echo "Health check failed with status code: $status_code"
                        exit 1
                    else
                        echo "Health check passed with status code: $status_code"
                    fi
                '''
            }
        }
    }
}
