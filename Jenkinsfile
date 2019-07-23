pipeline {
  agent {
    node {
      label 'jslave-PSI-azure1'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Building...'
      }
    }
    stage('Test1') {
      steps {
        echo 'Test1...'
      }
    }
  }
  environment {
    MSG = 'hello'
  }
}