pipeline {
   agent any

   stages {
      stage('Hello') {
         steps {
            catchError(message: 'Fetch code from Github failed') {
    // some block
            git 'https://github.com/kalikichandu/DevOps-for-ML.git'
            }
            dir('DevOps-for-ML') {
                // some block
                pwd()
                fileExists '/Dockerfile'
            }
         }
      }
   }
}
