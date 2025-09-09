pipeline {
  agent any

  environment {
  DOCKERHUB_CREDSID = 'DOCKERHUB_CREDS'               // From Jenkins credentials
  IMAGE_NAME        = 'piyushgupta2004/flask-app'     // From your Docker Hub repo
  PUSH_LATEST       = 'true'
}

  options {
    timestamps()
    ansiColor('xterm')
    buildDiscarder(logRotator(numToKeepStr: '20'))
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Compute Timestamp Tag') {
      steps {
        script {
          env.IMG_TAG = sh(returnStdout: true, script: "date -u +%Y%m%d%H%M%S").trim()
          echo "Timestamp tag: ${env.IMG_TAG}"
        }
      }
    }

    stage('Docker Build') {
      steps {
        sh """
          set -eux
          docker build -t ${IMAGE_NAME}:${IMG_TAG} .
        """
      }
    }

    stage('Docker Login & Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: "${DOCKERHUB_CREDSID}", usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
          sh 'echo "$DH_PASS" | docker login -u "$DH_USER" --password-stdin'
        }
        sh """
          set -eux
          docker push ${IMAGE_NAME}:${IMG_TAG}
          if [ "${PUSH_LATEST}" = "true" ]; then
            docker tag ${IMAGE_NAME}:${IMG_TAG} ${IMAGE_NAME}:latest
            docker push ${IMAGE_NAME}:latest
          fi
        """
      }
    }
  }

  post {
    success {
      echo "Pushed: ${IMAGE_NAME}:${IMG_TAG}"
    }
    always {
      // safe cleanup
      sh 'docker image prune -f || true'
    }
  }
}

