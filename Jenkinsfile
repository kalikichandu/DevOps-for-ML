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
      stage('Build and Run Docker Container') {
         steps {
            script {
                  sh 'chmod 700 ${WORKSPACE}/Dockerfile'
                  sh 'scp ${WORKSPACE}/Dockerfile azure_prod@104.43.164.138:/var/house_price_prediction_api/'
                  sh 'scp ${WORKSPACE}/CI_and_CD/src/inference.py azure_prod@104.43.164.138:/var/house_price_prediction_api/CI_and_CD/src/'

                  sh 'ssh azure_prod@104.43.164.138 cd /var/house_price_prediction_api/'
                  sh 'ssh azure_prod@104.43.164.138 sudo docker build --tag ml_api .'

                  sh 'ssh azure_prod@104.43.164.138 sudo docker run -d -p 5000:5000 -v ml_vol:/var/house_price_prediction/ ml_api'

            }
          
         }
      }

   }
}
