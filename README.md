* run bash <b>deploy.sh</b> to build the image and run the container

'''
<b>docker build -t sonova-test-app:new . </b>
<b>docker run -d -p 8080:8080 --name sonova-api sonova-test-app:new</b>
'''

* run this code to execute the tests:
'''
    <b>docker exec -it sonova-api pytest --ignore=tests/ --cov=app tests/ --cov-config=.coveragerc</b>
'''

* execute below  command lines to deploy image on GCP Container Registery
'''
<b>gcloud auth configure-docker
<b>gcloud config set project trading-320216
<b>gcloud builds submit --tag gcr.io/trading-320216/sonova-api
'''

*  deploy it on Cloud Run
* Final URL is:
<https://sonova-api-4ivksk4oza-pd.a.run.app/docs>

* Sample request:
'''
curl -X 'POST' \
  'https://sonova-api-4ivksk4oza-pd.a.run.app/v1/location/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data": [
    [
      0.65,
      0.43
    ]
  ]
}'
'''