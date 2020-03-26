pipeline {
   agent any

   stages {
      stage('Clone New Code') {
         steps {
            cleanWs()
            git 'https://github.com/kalikichandu/DevOps-for-ML.git'
            sh 'pwd'
            sh 'ls -lah'
          
         }
      }
   }
}
