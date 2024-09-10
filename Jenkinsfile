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
		        sh 'docker push 392209090241.dkr.ecr.eu-central-1.amazonaws.com/myecr:$GIT_COMMIT'
            }
        }
    }
}
