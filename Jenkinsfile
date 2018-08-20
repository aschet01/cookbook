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
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
