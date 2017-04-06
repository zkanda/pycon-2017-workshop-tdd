pipeline {
  agent any
  stages {
    stage('error') {
      steps {
        sh '''pip install django
cd sms_survey
./manage.py test'''
      }
    }
  }
}