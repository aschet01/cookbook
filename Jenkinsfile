/* Run `~/Documents/Code/ngrok.exe http 8080 
 *   and navigate to the URL it is forwarding.
 * Access ngrok administration at localhost:4040.
 */
pipeline {
    agent any
    environment {
        JENKINS_ROOT = "${JENKINS_HOME}"
    }
    stages {
        stage('Build') {
            steps {
                echo "Build ${env.BUILD_ID} for Job ${env.JOB_ID} on ${env.JENKINS_URL}"
                sh 'env'
            }
        }
        stage('Test') {
            steps {
                sh 'pwd; ls -al'
                sh 'python -m unittest python/_unittest.py'
                sh 'env'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'env'
            }
        }
    }
}
