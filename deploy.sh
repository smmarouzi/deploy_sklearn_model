docker build -t sonova-test-app:new .
docker run -d -p 80:80 --name sonova-api sonova-test-app:new

gcloud config set project trading-320216
gcloud builds submit --tag gcr.io/trading-320216/myimage