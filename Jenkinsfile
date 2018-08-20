/* Run `~/Documents/Code/ngrok.exe http 8080 
 *   and navigate to the URL it is forwarding.
 * Access ngrok administration at localhost:4040.
 */
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'env'
            }
        }
        stage('Test') {
            steps {
                sh 'pwd; echo; ls -al'
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
