pipeline {
  agent {
    docker {
      image 'python'
    }
    
  }
  stages {
    stage('') {
      steps {
        sh '''pip install django
cd sms_survey
./manage.py test'''
      }
    }
  }
}