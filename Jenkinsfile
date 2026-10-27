pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/stuckedinthe-loop/html-form-jenkins.git'
            }
        }

        stage('Test HTML Form') {
            steps {
                bat 'python test_form.py'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: All HTML form tests passed!'
        }
        failure {
            echo 'FAILURE: HTML form tests failed!'
        }
    }
}
