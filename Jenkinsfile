pipeline {
    agent any
    stages {
        stage('Setup parameters') {
            steps {
                script { 
                    properties([
                        parameters([
                            string( 
                                defaultValue: 'http://<URL>:<PORT>',
                                name: 'URL',
                                trim: true
                            )
                        ])
                    ])
                }
            }
        }
        stage('Run Test') {
            steps {
                sh 'export URL=params.URL && pytest ./test.py  -sv --html report.html'
            }
        }
    }
}
