docker build -t sonova-test-app:new .
docker run -d -p 8080:8080 --name sonova-api sonova-test-app:new

gcloud auth configure-docker
gcloud config set project trading-320216
gcloud builds submit --tag gcr.io/trading-320216/sonova-api

https://sonova-api-4ivksk4oza-pd.a.run.app/docs

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