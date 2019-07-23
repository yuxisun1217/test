pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }
    stage('Test1') {
      parallel {
        stage('Test1') {
          steps {
            echo 'Test1...'
          }
        }
        stage('Test2') {
          steps {
            sh 'echo "Test2...."'
          }
        }
      }
    }
  }
}