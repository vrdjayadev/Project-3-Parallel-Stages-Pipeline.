pipeline {
    agent any

    stages {
        stage('Parallel Academic Validations') {
            parallel {
                stage('Profile Structural Check') {
                    steps {
                        echo 'Triggering automated student data structure audit...'
                        sh 'python3 student_check.py'
                    }
                }
                stage('Academic Formula Audit') {
                    steps {
                        echo 'Triggering automated score system formula validation...'
                        sh 'python3 academic_check.py'
                    }
                }
            }
        }
        stage('Pipeline Completion Summary') {
            steps {
                echo 'CI/CD pipeline stage execution complete.'
                echo 'Both independent academic sub-modules have executed concurrently.'
            }
        }
    }
}
