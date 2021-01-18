node {

    stage("Checkout repo") {
        git branch: 'master',
        url: 'https://github.com/alex-radchenko-github/page_object_example'
    }
    stage("requirements") {
        sh 'pip3 install -r requirements.txt'
    }
    stage("test") {
        sh 'pipenv run pytest -s -v --br_type=chrome --selenoid=serv TestSmokeTesting.py -sv --alluredir=allure_result'
    }
    stage("report") {
        script {
                allure([
                    includeProperties: false,
                    jdk: '',
                    properties: [],
                    reportBuildPolicy: 'ALWAYS',
                    results: [[path: 'allure_result']]
                ])
        }
    }
}